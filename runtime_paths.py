from __future__ import annotations

import os
import sys
from pathlib import Path


def _application_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def _assets_root() -> Path:
    override = os.environ.get("LST_ASSETS_DIR")
    if override:
        return Path(override).expanduser().resolve()

    app_dir = _application_dir()

    # Final onedir layout: bundled runtime/assets live next to the main executable.
    if getattr(sys, "frozen", False):
        return app_dir

    # Development layout:
    # C:\local_screen_translator\local_screen_translator\*.py
    # C:\local_screen_translator\release_assets\...
    sibling = app_dir.parent / "release_assets"
    if sibling.exists():
        return sibling

    # Optional fallback for a release_assets folder placed inside the source tree.
    return app_dir / "release_assets"


APP_DIR = _application_dir()
ASSETS_ROOT = _assets_root()

OLLAMA_DIR = ASSETS_ROOT / "ollama"
OLLAMA_EXE = OLLAMA_DIR / "ollama.exe"
OLLAMA_MODELS_DIR = ASSETS_ROOT / "models" / "ollama"

PADDLE_MODELS_DIR = ASSETS_ROOT / "models" / "paddle"
PADDLE_DET_MODEL_DIR = PADDLE_MODELS_DIR / "PP-OCRv6_small_det"
PADDLE_REC_MODEL_DIR = PADDLE_MODELS_DIR / "latin_PP-OCRv5_mobile_rec"

BERT_MODEL_DIR = ASSETS_ROOT / "models" / "bert-base-multilingual-cased"

# Standalone PyInstaller build of align_worker.py.
# Development:
#   C:\local_screen_translator\release_assets\align\LSTAlignWorker\LSTAlignWorker.exe
# Frozen release:
#   <app_dir>\align\LSTAlignWorker\LSTAlignWorker.exe
ALIGN_WORKER_DIR = ASSETS_ROOT / "align" / "LSTAlignWorker"
ALIGN_WORKER_EXE = ALIGN_WORKER_DIR / "LSTAlignWorker.exe"
