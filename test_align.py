import time
from simalign import SentenceAligner

src = [
    "She", "shrugged", "."
]

trg = [
    "Она", "пожала", "плечами", "."
]

print("Loading model...")
t0 = time.perf_counter()

aligner = SentenceAligner(
    model="bert",
    token_type="bpe",
    matching_methods="mai",
)

t1 = time.perf_counter()

print(f"MODEL LOAD: {t1 - t0:.3f}s")
print()

for n in range(1, 6):
    start = time.perf_counter()

    alignments = aligner.get_word_aligns(src, trg)

    end = time.perf_counter()

    matches = [
        trg[j]
        for i, j in alignments["itermax"]
        if src[i] == "shrugged"
    ]

    print(
        f"RUN {n}: {end - start:.3f}s | "
        f"shrugged -> {' '.join(matches)}"
    )