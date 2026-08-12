from __future__ import annotations

import json

import requests


class LogicBridgeError(RuntimeError):
    pass


class LogicBridge:
    def __init__(
        self,
        ollama_url: str = "http://127.0.0.1:11434/api/chat",
        model: str = "qwen3:4b",
    ) -> None:
        self.ollama_url = ollama_url
        self.model = model

        self.schema = {
            "type": "object",
            "properties": {
                "source_span": {
                    "type": "string",
                },
                "translation": {
                    "type": "string",
                },
            },
            "required": [
                "source_span",
                "translation",
            ],
            "additionalProperties": False,
        }

        self.system_prompt = """
You produce a contextual Russian dictionary translation for a word
selected by the user.

You receive:

SOURCE:
The original English context.

TARGET_WORD:
The exact English word selected by the user.

SENTENCE_TRANSLATION:
A correct Russian translation of SOURCE.

Return:
- source_span
- translation

source_span rules:
- source_span MUST contain TARGET_WORD.
- Normally source_span is exactly TARGET_WORD.
- Expand it only when TARGET_WORD is part of a phrasal verb, idiom,
  or fixed expression whose meaning belongs to the whole expression.
- Return the shortest meaningful expression.
- Do not include optional subjects, objects, adjectives, or adverbs.
- Preserve the English grammatical form found in SOURCE.

translation rules:
- Translate source_span according to its meaning in SOURCE.
- Return a Russian dictionary-style translation, not the whole sentence.
- Use SENTENCE_TRANSLATION as semantic evidence.
- The Russian equivalent may be implicit rather than literally present
  as one word in SENTENCE_TRANSLATION.
- Prefer dictionary form:
  noun -> nominative singular
  verb -> infinitive
  adjective -> base masculine singular form.
- Preserve a multiword Russian expression when required.

Examples:

SOURCE:
He gave up immediately.
TARGET_WORD:
up
SENTENCE_TRANSLATION:
Он сразу же отказался.
RESULT:
source_span = gave up
translation = отказаться

SOURCE:
She shrugged and walked away.
TARGET_WORD:
shrugged
SENTENCE_TRANSLATION:
Она пожала плечами и ушла.
RESULT:
source_span = shrugged
translation = пожать плечами

SOURCE:
Not even a groan?
TARGET_WORD:
groan
SENTENCE_TRANSLATION:
Ни одного стона?
RESULT:
source_span = groan
translation = стон
""".strip()

    def resolve(
        self,
        source: str,
        target_word: str,
        sentence_translation: str,
    ) -> dict[str, str]:
        user_prompt = f"""
SOURCE:
{source}

TARGET_WORD:
{target_word}

SENTENCE_TRANSLATION:
{sentence_translation}
""".strip()

        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                "stream": False,
                "think": False,
                "format": self.schema,
                "options": {
                    "temperature": 0,
                    "seed": 42,
                    "num_predict": 50,
                    "num_ctx": 1024,
                },
                "keep_alive": "10m",
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        try:
            result = json.loads(
                data["message"]["content"]
            )
        except Exception as exc:
            raise LogicBridgeError(
                f"Invalid Logic model response: {exc}"
            ) from exc

        source_span = result.get(
            "source_span",
            "",
        ).strip()

        translation = result.get(
            "translation",
            "",
        ).strip()

        if not source_span:
            raise LogicBridgeError(
                "Logic model returned empty source_span"
            )

        if not translation:
            raise LogicBridgeError(
                "Logic model returned empty translation"
            )

        normalized_source = " ".join(source.split())
        normalized_span = " ".join(source_span.split())
        normalized_word = " ".join(target_word.split())

        if (
            normalized_span.casefold()
            not in normalized_source.casefold()
        ):
            raise LogicBridgeError(
                f"source_span is not present in SOURCE: "
                f"{source_span!r}"
            )

        if (
            normalized_word.casefold()
            not in normalized_span.casefold()
        ):
            raise LogicBridgeError(
                f"source_span does not contain TARGET_WORD: "
                f"{source_span!r}"
            )

        return {
            "source_span": normalized_span,
            "translation": translation,
        }


if __name__ == "__main__":
    bridge = LogicBridge()

    result = bridge.resolve(
        source="He turned down the offer immediately.",
        target_word="down",
        sentence_translation="Он сразу отклонил предложение.",
    )

    print(
        "SOURCE SPAN:",
        repr(result["source_span"]),
    )

    print(
        "TRANSLATION:",
        repr(result["translation"]),
    )