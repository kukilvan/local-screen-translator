import re
import requests

from align_client import AlignClient


SOURCE = "She shrugged."
TARGET_WORD = "shrugged"

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
RIVA_MODEL = "riva-en-ru"


def tokenize(text: str):
    return re.findall(r"\w+(?:['’-]\w+)*|[^\w\s]", text, re.UNICODE)


response = requests.post(
    OLLAMA_URL,
    json={
        "model": RIVA_MODEL,
        "prompt": SOURCE,
        "stream": False,
        "keep_alive": "10m",
    },
    timeout=60,
)

response.raise_for_status()

data = response.json()
translation = data["response"].strip()

src = tokenize(SOURCE)
trg = tokenize(translation)

target_index = next(
    i
    for i, word in enumerate(src)
    if word.lower() == TARGET_WORD.lower()
)

print("SOURCE:")
print(SOURCE)

print("\nTRANSLATION:")
print(translation)

print("\nSRC TOKENS:")
print(src)

print("\nTRG TOKENS:")
print(trg)

client = AlignClient()

try:
    result = client.align(
        src=src,
        trg=trg,
        target_index=target_index,
    )

    print("\nALIGNMENT:")
    print(result)

finally:
    client.close()