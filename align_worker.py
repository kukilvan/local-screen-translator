import json
import sys

from simalign import SentenceAligner


def send(data):
    print(json.dumps(data, ensure_ascii=False), flush=True)


aligner = SentenceAligner(
    model="bert",
    token_type="bpe",
    matching_methods="mai",
)

send({"status": "ready"})


for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        request = json.loads(line)

        src = request["src"]
        trg = request["trg"]
        target_index = request["target_index"]

        alignments = aligner.get_word_aligns(src, trg)

        result = {}

        for method, pairs in alignments.items():
            target_indices = sorted(
                j for i, j in pairs
                if i == target_index
            )

            result[method] = {
                "indices": target_indices,
                "words": [trg[j] for j in target_indices],
            }

        send({
            "status": "ok",
            "source_word": src[target_index],
            "alignments": result,
        })

    except Exception as exc:
        send({
            "status": "error",
            "error": str(exc),
        })