import json
import time

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3:1.7b"


schema = {
    "type": "object",
    "properties": {
        "source_span": {
            "type": "string"
        },
        "target_span": {
            "type": "string"
        },
    },
    "required": [
        "source_span",
        "target_span",
    ],
    "additionalProperties": False,
}


system_prompt = """
You are a semantic alignment tool.

You receive:
1. SOURCE: an English sentence.
2. TARGET_WORD: one English word selected by the user.
3. TRANSLATION: an already completed Russian translation of SOURCE.

Your job is NOT to translate the sentence.

Find the shortest meaningful English lexical unit containing TARGET_WORD,
then find its exact semantic equivalent in TRANSLATION.

The source_span must contain ONLY the minimal lexical unit needed to preserve
the contextual meaning of TARGET_WORD.

Never include optional adverbs, adjectives, objects, subjects, or other
surrounding words unless they are an inseparable part of the expression.

For phrasal verbs, include the verb and required particle only.

Examples:
gave up immediately -> gave up
looked after the child -> looked after
turned the light off -> turned off

Important rules:

- source_span MUST be copied exactly from SOURCE.
- target_span MUST be copied exactly from TRANSLATION.
- If TARGET_WORD is part of a phrasal verb, idiom, or fixed expression,
  source_span MUST include the complete expression.
- Do not force an isolated word-to-word correspondence when the meaning
  belongs to a multi-word expression.
- target_span may contain one or several words.
- Do not change grammatical forms.
- Do not invent words that are absent from SOURCE or TRANSLATION.

Examples:

SOURCE:
Not even a groan?
TARGET_WORD:
groan
TRANSLATION:
Ни одного стона?
RESULT:
source_span = groan
target_span = стона

SOURCE:
He gave me a hand.
TARGET_WORD:
hand
TRANSLATION:
Он мне помог.
RESULT:
source_span = gave me a hand
target_span = помог
""".strip()


user_prompt = """
SOURCE:
He gave up immediately.

TARGET_WORD:
up

TRANSLATION:
Он сразу же отказался.
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
        },
        "keep_alive": "5m",
    },
    timeout=60,
)

response.raise_for_status()

t1 = time.perf_counter()

data = response.json()
result = json.loads(
    data["message"]["content"]
)

print("SOURCE SPAN:", repr(result["source_span"]))
print("TARGET SPAN:", repr(result["target_span"]))
print(f"TIME: {t1 - t0:.3f}s")