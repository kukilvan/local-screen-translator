from __future__ import annotations

import subprocess
import time
from pathlib import Path

import requests


OLLAMA_EXE = (
    r"C:\Users\erudi\AppData\Local\Programs\Ollama\ollama.exe"
)

MODEL = "riva-dict-test"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

MODELFILE = r'''
FROM hf.co/liodon-ai/Riva-Translate-4B-Instruct-v2-imatrix-GGUF:Q6_K

TEMPLATE """<s>System
You are a contextual English-Russian dictionary.

The user gives:
SOURCE: the complete English context.
TARGET: the English word or expression to translate.

Translate TARGET according to its meaning in SOURCE.

Rules:
- Output ONLY the Russian translation.
- Do not translate the whole SOURCE.
- Do not explain anything.
- Preserve the contextual meaning.
- Prefer dictionary form when natural:
  nouns -> nominative singular,
  verbs -> infinitive,
  adjectives -> base form.
- For phrasal verbs, idioms, and fixed expressions, translate the whole expression.
</s>
<s>User
{{ .Prompt }}</s>
<s>Assistant
{{ .Response }}"""

PARAMETER temperature 0
PARAMETER seed 42
PARAMETER num_ctx 2048
PARAMETER stop "</s>"
'''.strip()


def ensure_model() -> None:
    result = subprocess.run(
        [
            OLLAMA_EXE,
            "show",
            MODEL,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        return

    modelfile_path = Path("Modelfile.riva_dict_test")
    modelfile_path.write_text(
        MODELFILE,
        encoding="utf-8",
    )

    print("Creating riva-dict-test...")

    subprocess.run(
        [
            OLLAMA_EXE,
            "create",
            MODEL,
            "-f",
            str(modelfile_path),
        ],
        check=True,
    )


def translate(
    source: str,
    target: str,
) -> tuple[str, float]:
    prompt = f"""SOURCE:
{source}

TARGET:
{target}
"""

    t0 = time.perf_counter()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "10m",
            "options": {
                "temperature": 0,
                "seed": 42,
                "num_predict": 40,
            },
        },
        timeout=60,
    )

    response.raise_for_status()

    elapsed = time.perf_counter() - t0

    return (
        response.json()["response"].strip(),
        elapsed,
    )


ensure_model()

tests = [
    (
        "Not even a groan? How disappointing.",
        "groan",
    ),
    (
        "Not even a groan? How disappointing.",
        "even",
    ),
    (
        "He gave up immediately.",
        "gave up",
    ),
    (
        "He looked after the child.",
        "looked after",
    ),
]

for source, target in tests:
    result, elapsed = translate(
        source,
        target,
    )

    print()
    print("SOURCE:", repr(source))
    print("TARGET:", repr(target))
    print("RIVA:", repr(result))
    print(f"TIME: {elapsed:.3f}s")
