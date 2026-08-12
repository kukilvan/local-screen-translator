from __future__ import annotations

import json
import time

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3:4b"


schema = {
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


system_prompt = """
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


user_prompt = """
SOURCE:
Not even a groan? How disappointing.

TARGET_WORD:
even

SENTENCE_TRANSLATION:
Ни одного стона? Как разочаровательно.
""".strip()


t0 = time.perf_counter()

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        "stream": False,
        "think": False,
        "format": schema,
        "options": {
            "temperature": 0,
            "seed": 42,
            "num_predict": 30,
            "num_ctx": 1024,
        },
        "keep_alive": "10m",
    },
    timeout=30,
)

response.raise_for_status()

data = response.json()
result = json.loads(data["message"]["content"])

elapsed = time.perf_counter() - t0

print("SOURCE SPAN:", repr(result["source_span"]))
print("TRANSLATION:", repr(result["translation"]))
print(f"TIME: {elapsed:.3f}s")
