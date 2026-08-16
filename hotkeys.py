from __future__ import annotations

import ctypes
import ctypes.wintypes as wintypes
import threading

from PySide6.QtCore import QObject, Signal

from config import (
    MOD_ALT,
    MOD_CONTROL,
    MOD_NOREPEAT,
    MOD_SHIFT,
    SETTINGS,
)
from user_settings import USER_SETTINGS
from ui_i18n import t


WM_HOTKEY = 0x0312
WM_QUIT = 0x0012

HOTKEY_WORD = 1
HOTKEY_PARAGRAPH = 2


def _hotkey_registration_error(
    hotkey: str,
) -> str:
    return t(
        "error",
        error=(
            f"Could not register hotkey {hotkey}. "
            "The shortcut may already be used by another application."
        ),
    )


def parse_hotkey(
    hotkey: str,
) -> tuple[int, int]:
    parts = [
        part.strip().lower()
        for part in hotkey.split("+")
        if part.strip()
    ]

    modifiers = MOD_NOREPEAT
    key_vk = None

    for part in parts:
        if part in (
            "ctrl",
            "control",
        ):
            modifiers |= MOD_CONTROL

        elif part == "alt":
            modifiers |= MOD_ALT

        elif part == "shift":
            modifiers |= MOD_SHIFT

        elif part == "space":
            key_vk = 0x20

        elif (
            len(part) == 1
            and "a" <= part <= "z"
        ):
            key_vk = ord(
                part.upper()
            )

        elif (
            len(part) == 1
            and "0" <= part <= "9"
        ):
            key_vk = ord(part)

        elif (
            part.startswith("f")
            and part[1:].isdigit()
        ):
            function_number = int(
                part[1:]
            )

            if not 1 <= function_number <= 24:
                raise ValueError(
                    f"Unsupported hotkey: {hotkey}"
                )

            key_vk = (
                0x70
                + function_number
                - 1
            )

        else:
            raise ValueError(
                f"Unsupported hotkey: {hotkey}"
            )

    if key_vk is None:
        raise ValueError(
            f"Hotkey has no key: {hotkey}"
        )

    return (
        modifiers,
        key_vk,
    )


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", wintypes.LONG),
        ("y", wintypes.LONG),
    ]


class MSG(ctypes.Structure):
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("message", wintypes.UINT),
        ("wParam", wintypes.WPARAM),
        ("lParam", wintypes.LPARAM),
        ("time", wintypes.DWORD),
        ("pt", POINT),
        ("lPrivate", wintypes.DWORD),
    ]


class GlobalHotkeys(QObject):
    triggered = Signal(str)
    error = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._thread: threading.Thread | None = None
        self._thread_id: int | None = None
        self._stop_requested = threading.Event()

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_requested.clear()
        self._thread = threading.Thread(
            target=self._message_loop,
            name="Win32HotkeyLoop",
            daemon=True,
        )
        self._thread.start()

    def stop(self) -> None:
        self._stop_requested.set()

        if self._thread_id is not None:
            ctypes.windll.user32.PostThreadMessageW(
                self._thread_id,
                WM_QUIT,
                0,
                0,
            )

        if (
            self._thread is not None
            and self._thread is not threading.current_thread()
        ):
            self._thread.join(
                timeout=2.0
            )

        self._thread = None

    def restart(self) -> None:
        self.stop()
        self.start()

    def _message_loop(self) -> None:
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        self._thread_id = int(kernel32.GetCurrentThreadId())

        (
            word_hotkey_mods,
            word_hotkey_vk,
        ) = parse_hotkey(
            USER_SETTINGS.word_hotkey
        )

        registered_word = bool(
            user32.RegisterHotKey(
                None,
                HOTKEY_WORD,
                word_hotkey_mods,
                word_hotkey_vk,
            )
        )
        (
            paragraph_hotkey_mods,
            paragraph_hotkey_vk,
        ) = parse_hotkey(
            USER_SETTINGS.paragraph_hotkey
        )

        registered_paragraph = bool(
            user32.RegisterHotKey(
                None,
                HOTKEY_PARAGRAPH,
                paragraph_hotkey_mods,
                paragraph_hotkey_vk,
            )
        )

        if not registered_word:
            self.error.emit(
                _hotkey_registration_error(
                    USER_SETTINGS.word_hotkey
                )
            )

        if not registered_paragraph:
            self.error.emit(
                _hotkey_registration_error(
                    USER_SETTINGS.paragraph_hotkey
                )
            )

        msg = MSG()

        try:
            while not self._stop_requested.is_set():
                result = user32.GetMessageW(
                    ctypes.byref(msg),
                    None,
                    0,
                    0,
                )
                if result <= 0:
                    break

                if msg.message == WM_HOTKEY:
                    if msg.wParam == HOTKEY_WORD:
                        self.triggered.emit("word")
                    elif msg.wParam == HOTKEY_PARAGRAPH:
                        self.triggered.emit("paragraph")
        finally:
            if registered_word:
                user32.UnregisterHotKey(None, HOTKEY_WORD)
            if registered_paragraph:
                user32.UnregisterHotKey(None, HOTKEY_PARAGRAPH)
            self._thread_id = None
