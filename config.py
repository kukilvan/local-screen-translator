from dataclasses import dataclass
from typing import Optional


# Win32 modifier constants used by RegisterHotKey.
MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
MOD_NOREPEAT = 0x4000

VK_SPACE = 0x20


@dataclass(frozen=True)
class Settings:
    # -------- Ollama --------
    ollama_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen2.5:7b-instruct-q4_0"
    target_language: str = "Russian"
    ollama_keep_alive: int | str = -1
    ollama_num_ctx: int = 2048
    ollama_timeout_seconds: float = 25.0

    # -------- OCR --------
    # Windows OCR language pack. For English games use en-US.
    ocr_language: str = "en-US"
    ocr_scale: float = 1.0

    # Word mode reads a compact block around the mouse.
    word_roi_width: int = 500
    word_roi_height: int = 110

    # Paragraph mode intentionally reads a larger area.
    paragraph_roi_width: int = 1500
    paragraph_roi_height: int = 260

    # How far the mouse may be from a recognized word/line before we reject it.
    max_word_distance_px: float = 70.0
    max_paragraph_distance_px: float = 110.0

    # -------- DXcam --------
    # None = primary output on the chosen DXGI adapter.
    # Run:
    #   python -c "import dxcam; print(dxcam.device_info()); print(dxcam.output_info())"
    # to inspect indexes when the game is on a non-primary monitor.
    capture_device_idx: int = 0
    capture_output_idx: Optional[int] = None
    capture_backend: str = "dxgi"  # "dxgi" first; "winrt" is a fallback.

    # -------- Hotkeys --------
    # WORD:      Ctrl + Alt + Space
    # PARAGRAPH: Ctrl + Alt + Shift + Space
    word_hotkey_mods: int = MOD_CONTROL | MOD_ALT | MOD_NOREPEAT
    paragraph_hotkey_mods: int = MOD_CONTROL | MOD_ALT | MOD_SHIFT | MOD_NOREPEAT
    hotkey_vk: int = VK_SPACE

    # -------- HUD --------
    hud_max_width: int = 620
    hud_auto_hide_ms: int = 12000
    hud_offset_x: int = 18
    hud_offset_y: int = 24


SETTINGS = Settings()
