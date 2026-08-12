import os
os.environ["FLAGS_enable_pir_api"] = "0"
from paddleocr import PaddleOCR
from pathlib import Path
import json

img_path = Path(__file__).resolve().parent / "ocr_test.png"

ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv6_small_det",
    text_recognition_model_name="PP-OCRv6_small_rec",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    enable_mkldnn=False,
    return_word_box=True,
    engine="paddle",
)

result = ocr.predict(str(img_path))

print("=== RAW RESULT ===")
print(result)

print("\n=== EXTRACTED TEXT ===")
texts = []

for item in result:
    rec_texts = item.get("rec_texts", [])
    for t in rec_texts:
        if t and str(t).strip():
            texts.append(str(t).strip())

print(" ".join(texts))

print("\n=== PRETTY JSON ===")
print(json.dumps(result, ensure_ascii=False, indent=2, default=str))

import time

print("\n=== SPEED TEST ===")

for i in range(5):
    start = time.perf_counter()
    ocr.predict(str(img_path))
    elapsed = (time.perf_counter() - start) * 1000
    print(f"Run {i + 1}: {elapsed:.1f} ms")