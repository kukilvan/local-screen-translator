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
    },
    "required": [
        "source_span",
    ],
    "additionalProperties": False,
}


system_prompt = """
You identify the minimal English lexical expression represented by a word
selected by the user.

You receive:
SOURCE: an English sentence.
TARGET_WORD: one word selected inside SOURCE.

Return source_span.

Rules:
- source_span MUST be copied exactly from SOURCE.
- source_span MUST contain TARGET_WORD.
- Normally return only TARGET_WORD.
- Expand it only if TARGET_WORD is part of a phrasal verb, idiom,
  or fixed expression whose contextual meaning belongs to the whole expression.
- Return the shortest possible expression.
- Never include optional subjects, objects, adjectives, or adverbs.

Examples:

SOURCE:
Not even a groan?
TARGET_WORD:
even
RESULT:
source_span = even

SOURCE:
Not even a groan?
TARGET_WORD:
groan
RESULT:
source_span = groan

SOURCE:
He gave up immediately.
TARGET_WORD:
up
RESULT:
source_span = gave up

SOURCE:
He looked after the child.
TARGET_WORD:
after
RESULT:
source_span = looked after
""".strip()


user_prompt = """
SOURCE:
He looked after the child.

TARGET_WORD:
after
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
        },
        "keep_alive": "10m",
    },
    timeout=30,
)

response.raise_for_status()

data = response.json()
result = json.loads(data["message"]["content"])

t1 = time.perf_counter()

print("SOURCE SPAN:", repr(result["source_span"]))
print(f"TIME: {t1 - t0:.3f}s")