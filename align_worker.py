import json
import os
import sys
from pathlib import Path


os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_DATASETS_OFFLINE", "1")

from simalign import SentenceAligner
from transformers import BertTokenizer


def send(data):
    print(json.dumps(data, ensure_ascii=True), flush=True)


model_dir_value = os.environ.get("LST_BERT_MODEL_DIR", "").strip()
if not model_dir_value:
    raise RuntimeError("LST_BERT_MODEL_DIR is not set")

model_dir = Path(model_dir_value).resolve()
if not model_dir.is_dir():
    raise RuntimeError(f"Bundled BERT model not found: {model_dir}")

# SimAlign's built-in model="bert" path uses BertTokenizer (the slow tokenizer).
# When we pass a local filesystem path, SimAlign falls back to AutoTokenizer,
# which may select BertTokenizerFast. With the current Transformers stack that
# fast tokenizer can reject some pre-tokenized paragraph batches with:
#   TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]]
#
# Keep the local/offline model, but restore the same slow BertTokenizer behavior
# as the original working model="bert" configuration.
aligner = SentenceAligner(
    model=str(model_dir),
    token_type="bpe",
    matching_methods="mai",
    device="cpu",
)

aligner.embed_loader.tokenizer = BertTokenizer.from_pretrained(
    str(model_dir),
    local_files_only=True,
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

        # Validate the protocol early and give a useful error instead of an
        # opaque tokenizer exception.
        if not isinstance(src, list) or not all(isinstance(x, str) for x in src):
            raise TypeError("src must be a list of strings")

        if not isinstance(trg, list) or not all(isinstance(x, str) for x in trg):
            raise TypeError("trg must be a list of strings")

        if not isinstance(target_index, int):
            raise TypeError("target_index must be an integer")

        if not src:
            raise ValueError("src is empty")

        if not trg:
            raise ValueError("trg is empty")

        if not 0 <= target_index < len(src):
            raise IndexError(
                f"target_index {target_index} is outside src length {len(src)}"
            )

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
