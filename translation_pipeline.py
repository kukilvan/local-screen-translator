import re
import time
import requests

from align_client import AlignClient
from logic_bridge import LogicBridge


class TranslationPipeline:
    def __init__(
        self,
        ollama_url="http://127.0.0.1:11434/api/generate",
        model="riva-en-ru",
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
        response = requests.post(
            self.ollama_url,
            json={
                "model": self.model,
                "prompt": text,
                "stream": False,
                "keep_alive": "10m",
            },
            timeout=60,
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    @staticmethod
    def _choose_alignment(alignments):
        """
        Выбираем наиболее надёжные target indices.

        1. Если >= 2 методов согласны по каждому индексу,
           используем эти индексы.
        2. Если такого нет — пробуем inter.
        3. Потом itermax.
        4. Потом mwmf.
        """

        votes = {}

        for data in alignments.values():
            for index in data["indices"]:
                votes[index] = votes.get(index, 0) + 1

        consensus = sorted(
            index
            for index, count in votes.items()
            if count >= 2
        )

        if consensus:
            return consensus

        for method in ("inter", "itermax", "mwmf"):
            indices = alignments.get(
                method,
                {},
            ).get(
                "indices",
                [],
            )

            if indices:
                return sorted(indices)

        return []

    def translate_with_alignment(
        self,
        text: str,
        target_word: str,
        target_occurrence: int = 0,
    ):
        timing_start = time.perf_counter()

        translation = self.translate(text)

        timing_riva = time.perf_counter()

        logic_result = self.logic.resolve(
            source=text,
            target_word=target_word,
            sentence_translation=translation,
        )

        timing_logic = time.perf_counter()

        source_span = logic_result["source_span"]

        source_span = logic_result["source_span"]

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
        print(
            "TARGET OCCURRENCE:",
            repr(target_word),
            f"#{target_occurrence + 1}",
            "token_index=",
            target_index,
            flush=True,
        )

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

        target_words = [
            trg_tokens[i]
            for i in target_indices
            if 0 <= i < len(trg_tokens)
        ]

        target_phrase = " ".join(
            target_words
        )
        timing_align = time.perf_counter()

        print(
            f"PIPELINE TIMING: "
            f"Riva={timing_riva - timing_start:.3f}s | "
            f"Logic={timing_logic - timing_riva:.3f}s | "
            f"SimAlign={timing_align - timing_logic:.3f}s | "
            f"TOTAL={timing_align - timing_start:.3f}s",
            flush=True,
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


if __name__ == "__main__":
    pipeline = TranslationPipeline()

    try:
        result = pipeline.translate_with_alignment(
            "She shrugged.",
            "shrugged",
        )

        print("SOURCE:")
        print(result["source_text"])

        print("\nTRANSLATION:")
        print(result["translation"])

        print("\nTARGET:")
        print(
            f'{result["source_word"]} -> '
            f'{result["target_phrase"]}'
        )

        print("\nTARGET INDICES:")
        print(result["target_indices"])

    finally:
        pipeline.close()