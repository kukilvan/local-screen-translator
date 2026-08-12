from __future__ import annotations

import ctypes
import ctypes.wintypes as wintypes
import threading

from PySide6.QtCore import QObject, Signal

from config import SETTINGS


WM_HOTKEY = 0x0312
WM_QUIT = 0x0012

HOTKEY_WORD = 1
HOTKEY_PARAGRAPH = 2


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

    def _message_loop(self) -> None:
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        self._thread_id = int(kernel32.GetCurrentThreadId())

        registered_word = bool(
            user32.RegisterHotKey(
                None,
                HOTKEY_WORD,
                SETTINGS.word_hotkey_mods,
                SETTINGS.hotkey_vk,
            )
        )
        registered_paragraph = bool(
            user32.RegisterHotKey(
                None,
                HOTKEY_PARAGRAPH,
                SETTINGS.paragraph_hotkey_mods,
                SETTINGS.hotkey_vk,
            )
        )

        if not registered_word:
            self.error.emit(
                "Не удалось зарегистрировать Ctrl+Alt+Space. "
                "Возможно, комбинация занята другой программой."
            )
        if not registered_paragraph:
            self.error.emit(
                "Не удалось зарегистрировать Ctrl+Alt+Shift+Space. "
                "Возможно, комбинация занята другой программой."
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
