import re

import requests

from align_client import AlignClient
from logic_bridge import LogicBridge

from user_settings import USER_SETTINGS
from config import SETTINGS


class TranslationPipeline:
    def __init__(
        self,
        ollama_url=f"{SETTINGS.ollama_url}/api/generate",
        model="riva-translate",
    ):
        self.ollama_url = ollama_url
        self.model = model

        # SimAlign загружается один раз и живёт вместе с приложением.
        self.aligner = AlignClient()
        self.logic = LogicBridge()

    @staticmethod
    def tokenize(text: str):
        return re.findall(
            r"\w+(?:['’-]\w+)*|[^\w\s]",
            text,
            re.UNICODE,
        )

    def translate(self, text: str) -> str:
        target_language = (
            USER_SETTINGS.target_language
        )

        system_prompt = (
            "You are an expert at translating text "
            f"from English to {target_language}."
        )

        translation_prompt = (
            f"What is the {target_language} translation "
            f"of the sentence: {text}"
        )

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "system": system_prompt,
                    "prompt": translation_prompt,
                    "stream": False,
                    "keep_alive": "10m",
                },
                timeout=60,
            )

            response.raise_for_status()

        except requests.RequestException as exc:
            raise RuntimeError(
                "LST-AI-001: Could not communicate with the "
                f"Riva translation model at {self.ollama_url}. "
                f"{type(exc).__name__}: {exc}"
            ) from exc

        try:
            data = response.json()
        except ValueError as exc:
            raise RuntimeError(
                "LST-AI-001: Riva returned invalid JSON."
            ) from exc

        if not isinstance(data, dict):
            raise RuntimeError(
                "LST-AI-001: Riva returned an unexpected response."
            )

        translation = data.get(
            "response",
            "",
        )

        if not isinstance(translation, str):
            raise RuntimeError(
                "LST-AI-001: Riva returned an invalid translation value."
            )

        translation = translation.strip()

        if not translation:
            raise RuntimeError(
                "LST-AI-001: Riva returned an empty translation."
            )

        return translation

    @staticmethod
    def _choose_alignment(alignments):
        def clean_indices(indices):
            indices = sorted(
                set(indices)
            )

            if not indices:
                return []

            max_tokens = 4
            max_span = 5

            if len(indices) > max_tokens:
                return []

            if (
                indices[-1]
                - indices[0]
                > max_span
            ):
                return []

            return indices

        votes = {}

        for data in alignments.values():
            for index in data["indices"]:
                votes[index] = (
                    votes.get(index, 0)
                    + 1
                )

        consensus = clean_indices(
            [
                index
                for index, count in votes.items()
                if count >= 2
            ]
        )

        if consensus:
            return consensus

        for method in (
            "inter",
            "itermax",
            "mwmf",
        ):
            indices = clean_indices(
                alignments.get(
                    method,
                    {},
                ).get(
                    "indices",
                    [],
                )
            )

            if indices:
                return indices

        return []

    @staticmethod
    def _find_phrase_indices(
        text_tokens,
        phrase_tokens,
    ):
        if not text_tokens or not phrase_tokens:
            return []

        text_folded = [
            token.casefold()
            for token in text_tokens
        ]

        phrase_folded = [
            token.casefold()
            for token in phrase_tokens
        ]

        size = len(phrase_folded)

        for start in range(
            len(text_folded) - size + 1
        ):
            if (
                text_folded[start:start + size]
                == phrase_folded
            ):
                return list(
                    range(
                        start,
                        start + size,
                    )
                )

        return []

    def translate_with_alignment(
        self,
        text: str,
        target_word: str,
        target_occurrence: int = 0,
    ):


        translation = self.translate(text)



        logic_result = self.logic.resolve(
            source=text,
            target_word=target_word,
            sentence_translation=translation,
            target_language=USER_SETTINGS.target_language,
        )



        source_span = logic_result["source_span"]
        dictionary_translation = logic_result["translation"]

        src_tokens = self.tokenize(text)
        trg_tokens = self.tokenize(translation)
        span_tokens = self.tokenize(source_span)

        matching_indices = [
            i
            for i, token in enumerate(src_tokens)
            if token.casefold() == target_word.casefold()
        ]

        if not matching_indices:
            raise ValueError(
                f"Target word not found in source tokens: "
                f"{target_word!r}"
            )

        if target_occurrence >= len(
            matching_indices
        ):
            raise ValueError(
                f"Target occurrence "
                f"{target_occurrence} is out of range "
                f"for {target_word!r}; "
                f"found {len(matching_indices)} occurrence(s)"
            )

        target_index = matching_indices[
            target_occurrence
        ]

        if target_index is None:
            raise ValueError(
                f"Target word not found: {target_word}"
            )

        source_indices = []

        if span_tokens:
            span_size = len(span_tokens)

            for start in range(
                0,
                len(src_tokens) - span_size + 1,
            ):
                candidate = src_tokens[
                    start:start + span_size
                ]

                if not all(
                    a.casefold() == b.casefold()
                    for a, b in zip(
                        candidate,
                        span_tokens,
                    )
                ):
                    continue

                candidate_indices = list(
                    range(
                        start,
                        start + span_size,
                    )
                )

                if target_index in candidate_indices:
                    source_indices = candidate_indices
                    break

        if not source_indices:
            source_indices = [
                target_index
            ]

        target_index_set = set()
        raw_alignments = {}

        # SimAlign не нужен весь огромный английский абзац.
        # Оставляем небольшой контекст вокруг выбранного выражения.
        context_tokens = 10

        window_start = max(
            0,
            min(source_indices) - context_tokens,
        )

        window_end = min(
            len(src_tokens),
            max(source_indices) + context_tokens + 1,
        )

        source_window = src_tokens[
            window_start:window_end
        ]

        for source_index in source_indices:
            local_source_index = (
                source_index - window_start
            )

            alignment = self.aligner.align(
                src=source_window,
                trg=trg_tokens,
                target_index=local_source_index,
            )

            raw_alignments[source_index] = alignment

            aligned_indices = self._choose_alignment(
                alignment["alignments"]
            )

            target_index_set.update(
                aligned_indices
            )

        target_indices = sorted(
            target_index_set
        )

        if not target_indices:
            dictionary_tokens = self.tokenize(
                dictionary_translation
            )

            target_indices = self._find_phrase_indices(
                trg_tokens,
                dictionary_tokens,
            )

        target_words = [
            trg_tokens[i]
            for i in target_indices
            if 0 <= i < len(trg_tokens)
        ]

        target_phrase = " ".join(
            target_words
        )




        return {
            "source_text": text,
            "source_word": target_word,
            "source_span": source_span,
            "source_indices": source_indices,
            "translation": translation,
            "source_tokens": src_tokens,
            "target_tokens": trg_tokens,
            "target_indices": target_indices,
            "target_phrase": target_phrase,
            "raw_alignment": raw_alignments,
        }

    def close(self):
        self.aligner.close()


