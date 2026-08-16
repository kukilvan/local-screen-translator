from __future__ import annotations

from urllib.parse import urlparse

import requests

from config import SETTINGS


class OllamaError(RuntimeError):
    pass


class OllamaClient:
    """
    Local-only client. It intentionally refuses non-loopback Ollama URLs.
    """

    def __init__(
        self,
        base_url: str = SETTINGS.ollama_url,
        model: str = SETTINGS.ollama_model,
        target_language: str = SETTINGS.target_language,
    ) -> None:
        parsed = urlparse(base_url)
        if parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError(
                "For privacy this build only allows a loopback Ollama server "
                "(127.0.0.1 / localhost / ::1)."
            )

        self.base_url = base_url.rstrip("/")
        self.model = model
        self.target_language = target_language
        self.session = requests.Session()

    def _chat(self, system: str, user: str, *, num_predict: int) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "think": False,
            "keep_alive": SETTINGS.ollama_keep_alive,
            "options": {
                "temperature": 0.0,
                "seed": 42,
                "num_ctx": SETTINGS.ollama_num_ctx,
                "num_predict": num_predict,
            },
        }

        try:
            response = self.session.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=SETTINGS.ollama_timeout_seconds,
            )
            response.raise_for_status()
            data = response.json()



        except requests.RequestException as exc:
            raise OllamaError(
                "LST-AI-001: Could not communicate with the local "
                f"Ollama server at {self.base_url}. "
                f"{type(exc).__name__}: {exc}"
            ) from exc
        except ValueError as exc:
            raise OllamaError(
                "LST-AI-001: Ollama returned invalid JSON from "
                f"{self.base_url}."
            ) from exc

        try:
            text = data["message"]["content"].strip()
        except (KeyError, TypeError, AttributeError) as exc:
            raise OllamaError(
                "LST-AI-001: Ollama returned an unexpected response: "
                f"{data!r}"
            ) from exc

        if not text:
            raise OllamaError(
                "LST-AI-001: Ollama returned an empty response "
                f"for model {self.model}."
            )
        return text

    def translate_word(self, word: str, context: str) -> str:
        system = f"""
You are a precise English-to-{self.target_language} dictionary translator
for video games.

The user points at ONE English word.
Translate that word itself.

The surrounding OCR text is ONLY context for:
- choosing between established meanings of the target word;
- determining its part of speech;
- understanding idioms or game terminology.

IMPORTANT:
- Do NOT invent a figurative meaning just because it seems to fit the sentence.
- Do NOT replace the word's lexical meaning with a description of the whole situation.
- Prefer the normal dictionary meaning that fits the grammar and context.
- Pay attention to articles and grammar to distinguish nouns, verbs, adjectives, etc.
- Treat the supplied TARGET WORD as correct unless the surrounding context gives very strong evidence of an OCR error.
- Silently correct obvious OCR errors only when virtually certain.
- For RPG/fantasy/game terminology, use the natural established {self.target_language} equivalent.
- Any optional note must be written in {self.target_language}.
- Never translate the whole surrounding sentence.
- Never explain your reasoning.

Output EXACTLY:

<English target word> → <best {self.target_language} translation>
<optional very short {self.target_language} context note>

The second line is optional and must be no longer than one short sentence.
""".strip()

        user = f"""
TARGET WORD:
{word}

SURROUNDING CONTEXT:
{context}
""".strip()

        return self._chat(system, user, num_predict=60)

    def translate_paragraph(self, text: str) -> str:
        system = f"""
You are a professional English-to-{self.target_language} video-game translator.

The input is OCR text captured from a game or application.
It may contain minor OCR errors. Correct only obvious OCR mistakes from context.

The marker <<<CURSOR>>> appears immediately before the English word
the user is pointing at.

Translate ALL supplied text into natural {self.target_language}.

Rules:
- Do not summarize, shorten, omit, or explain anything.
- Preserve meaning, tone, names, RPG terminology and dialogue style.
- Translate the entire supplied text.
- The marker <<<CURSOR>>> must appear exactly ONCE in your {self.target_language} translation.
- Move <<<CURSOR>>> so that it appears immediately before the {self.target_language} word
  or shortest {self.target_language} phrase corresponding to the English word it marked.
- Do not translate the marker itself.
- Output ONLY the translated {self.target_language} text.
- Do not add headings, notes or any other fields.


""".strip()

        return self._chat(system, text, num_predict=520)

    def preload(self) -> bool:
        """
        Ask Ollama to load the model into VRAM without generating text.
        Failure is intentionally non-fatal at app startup.
        """
        try:
            response = self.session.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.model,
                    "keep_alive": SETTINGS.ollama_keep_alive,
                },
                timeout=SETTINGS.ollama_timeout_seconds,
            )
            return response.ok
        except requests.RequestException:
            return False
