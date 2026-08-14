from __future__ import annotations
import traceback
import ctypes
import re
import os
import sys
import subprocess
import socket
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QStyle, QSystemTrayIcon
import time
from concurrent.futures import ThreadPoolExecutor
from settings_dialog import SettingsDialog
from user_settings import USER_SETTINGS
from PySide6.QtCore import QObject, Signal, Slot, QTimer
from PySide6.QtWidgets import QApplication

from capture_ocr import (
    ScreenOCR,
    choose_paragraph,
    choose_word,
    context_for_word,
)
from hotkeys import GlobalHotkeys
from hud import TranslationHUD
from llm_client import OllamaClient, OllamaError
from translation_pipeline import TranslationPipeline

from logic_bridge import LogicBridge, LogicBridgeError


CURSOR_MARKER = "<<<CURSOR>>>"
CURSOR_END_MARKER = "<<<END_CURSOR>>>"

TOKEN_RE = re.compile(
    r"\w+(?:['’-]\w+)*|[^\w\s]",
    re.UNICODE,
)


def enable_per_monitor_dpi_awareness() -> None:
    """
    Keep Win32 cursor pixels, DXGI pixels and Qt coordinates aligned,
    especially on multi-monitor systems with scaling.
    """
    try:
        DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = ctypes.c_void_p(-4)
        ctypes.windll.user32.SetProcessDpiAwarenessContext(
            DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
        )
    except Exception:
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            pass


def extract_cursor_word(
    marked_text: str,
) -> tuple[str, str, int]:
    """
    choose_paragraph() inserts <<<CURSOR>>> immediately
    before the source word under the mouse.

    Returns:
        clean_text
        target_word
        target_occurrence
    """
    marker_pos = marked_text.find(
        CURSOR_MARKER
    )

    if marker_pos < 0:
        raise ValueError(
            "Cursor marker was not found in OCR paragraph"
        )

    before_marker = marked_text[
        :marker_pos
    ]

    after_marker = marked_text[
        marker_pos + len(CURSOR_MARKER):
    ]

    match = re.search(
        r"\w+(?:['’-]\w+)*",
        after_marker,
        re.UNICODE,
    )

    if not match:
        raise ValueError(
            "Could not determine the word under the cursor"
        )

    target_word = match.group(0)

    target_occurrence = 0

    for previous_match in re.finditer(
        r"\w+(?:['’-]\w+)*",
        before_marker,
        re.UNICODE,
    ):
        if (
            previous_match.group(0).casefold()
            == target_word.casefold()
        ):
            target_occurrence += 1

    clean_text = marked_text.replace(
        CURSOR_MARKER,
        "",
        1,
    )

    return (
        clean_text,
        target_word,
        target_occurrence,
    )


def insert_cursor_markers_by_token_indices(
    text: str,
    token_indices: list[int],
) -> str:
    if not token_indices:
        return text

    matches = list(
        TOKEN_RE.finditer(text)
    )

    indices = sorted(
        set(token_indices)
    )

    if any(
        index < 0
        or index >= len(matches)
        for index in indices
    ):
        return text

    start_index = indices[0]
    end_index = indices[-1]

    span_length = (
        end_index
        - start_index
        + 1
    )

    if span_length > 4:
        return text

    for previous, current in zip(
        indices,
        indices[1:],
    ):
        if current - previous > 2:
            return text

    start_pos = matches[
        start_index
    ].start()

    end_pos = matches[
        end_index
    ].end()

    return (
        text[:start_pos]
        + CURSOR_MARKER
        + text[start_pos:end_pos]
        + CURSOR_END_MARKER
        + text[end_pos:]
    )


class WorkerSignals(QObject):
    done = Signal(int, str, int, int, object, object)
    failed = Signal(int, str, int, int)
    preload_status = Signal(bool)


class TranslatorController(QObject):
    def __init__(self, hud: TranslationHUD) -> None:
        super().__init__()

        self.hud = hud
        self.ocr = ScreenOCR()

        # Старый Qwen пока остаётся только для режима одного слова.
        self.llm = OllamaClient()

        # Новый pipeline:
        # Riva -> SimAlign.
        self.pipeline = TranslationPipeline()
        self.logic = LogicBridge()

        self.pool = ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix="TranslatorWorker",
        )

        self.signals = WorkerSignals()
        self.signals.done.connect(self._on_done)
        self.signals.failed.connect(self._on_failed)

        self._request_id = 0
        self._busy = False

        # Qwen специально больше не preload'им.
        # Иначе старый 7B сразу занимает VRAM даже тогда,
        # когда мы тестируем только Riva.


    @Slot(str)
    def trigger(self, mode: str) -> None:
        if self._busy:
            return

        self._busy = True
        self._request_id += 1
        request_id = self._request_id

        cursor_x, cursor_y = self.ocr.cursor_pos()

        # HUD обязательно скрываем ДО захвата экрана,
# чтобы собственное окно переводчика не попадало в OCR.
        self.hud.hide()

        QApplication.processEvents()

        QTimer.singleShot(
            50,
            lambda: self.pool.submit(
                self._process,
                request_id,
                mode,
                cursor_x,
                cursor_y,
            ),
        )


    def _process(
        self,
        request_id: int,
        mode: str,
        cursor_x: int,
        cursor_y: int,
    ) -> None:
        try:
            focus_rect = None
            if mode == "word":
                t0 = time.perf_counter()

                snapshot = None
                target = None
                marked_context = None

                for ocr_attempt in range(2):
                    try:
                        snapshot = self.ocr.snapshot_word_region(
                            (cursor_x, cursor_y)
                        )



                        target = choose_word(snapshot)



                        source_rect = (
                        int(
                            round(
                                cursor_x
                                - snapshot.cursor_x
                                + target.rect.x
                            )
                        ),
                        int(
                            round(
                                cursor_y
                                - snapshot.cursor_y
                                + target.rect.y
                            )
                        ),
                        int(
                            round(
                                target.rect.w
                            )
                        ),
                        int(
                            round(
                                target.rect.h
                            )
                        ),
                    )
                        marked_context = choose_paragraph(snapshot)

                        break

                    except Exception as ocr_exc:
                        if ocr_attempt == 0:
                            print(
                                "WORD OCR RETRY:",
                                repr(ocr_exc),
                                flush=True,
                            )
                            continue

                        raise

                t1 = time.perf_counter()

                context = marked_context.replace(
                    CURSOR_MARKER,
                    "",
                    1,
                ).strip()

                t2 = time.perf_counter()

                target_word = target.text

                sentence_translation = self.pipeline.translate(
                    context
                ).strip()

                t3 = time.perf_counter()

                try:
                    logic_result = self.logic.resolve(
                        source=context,
                        target_word=target.text,
                        sentence_translation=sentence_translation,
                        target_language=USER_SETTINGS.target_language,
                    )

                    source_span = logic_result["source_span"]
                    dictionary_translation = logic_result["translation"]
                    logic_used = True

                except Exception as logic_exc:
                    print(
                        "WORD LOGIC FALLBACK:",
                        repr(logic_exc),
                        flush=True,
                    )

                    source_span = target.text

                    dictionary_translation = self.pipeline.translate(
                        source_span
                    ).strip()

                    logic_used = False

                t4 = time.perf_counter()

                if not dictionary_translation:
                    raise RuntimeError(
                        f"Не удалось перевести {source_span!r}"
                    )

                translated = (
                    f"{source_span} → {dictionary_translation}"
                )








            elif mode == "paragraph":
                t0 = time.perf_counter()

                snapshot = self.ocr.snapshot_paragraph_region(
                    (cursor_x, cursor_y)
                )

                t1 = time.perf_counter()







                (
                    marked_paragraph,
                    paragraph_rect,
                ) = choose_paragraph(
                    snapshot,
                    return_rect=True,
                )

                source_rect = (

                    int(
                        round(
                            cursor_x
                            - snapshot.cursor_x
                            + paragraph_rect.x
                        )
                    ),
                    int(
                        round(
                            cursor_y
                            - snapshot.cursor_y
                            + paragraph_rect.y
                        )
                    ),
                    int(
                        round(
                            paragraph_rect.w
                        )
                    ),
                    int(
                        round(
                            paragraph_rect.h
                        )
                    ),
                )
                source_word_box = choose_word(
                    snapshot
                )

                focus_rect = (
                    int(
                        round(
                            cursor_x
                            - snapshot.cursor_x
                            + source_word_box.rect.x
                        )
                    ),
                    int(
                        round(
                            cursor_y
                            - snapshot.cursor_y
                            + source_word_box.rect.y
                        )
                    ),
                    int(
                        round(
                            source_word_box.rect.w
                        )
                    ),
                    int(
                        round(
                            source_word_box.rect.h
                        )
                    ),
                )
                t2 = time.perf_counter()

                (
                    paragraph,
                    target_word,
                    target_occurrence,
                ) = extract_cursor_word(
                    marked_paragraph
                )



                t3 = time.perf_counter()

                result = self.pipeline.translate_with_alignment(
                paragraph,
                target_word,
                target_occurrence,
                )

                t4 = time.perf_counter()

                translated = result["translation"]

                target_indices = result["target_indices"]
                target_phrase = result["target_phrase"]



                if target_indices:
                    translated = insert_cursor_markers_by_token_indices(
                        translated,
                        target_indices,
                    )





            else:
                raise ValueError(
                    f"Unknown mode: {mode}"
                )

            self.signals.done.emit(
                request_id,
                translated,
                cursor_x,
                cursor_y,
                source_rect,
                focus_rect,
            )

        except Exception as exc:
            print(
                "\n=== PROCESS ERROR ===",
                flush=True,
            )

            traceback.print_exc()

            print(
                "=== END PROCESS ERROR ===\n",
                flush=True,
            )

            self.signals.failed.emit(
                request_id,
                self._friendly_error(exc),
                cursor_x,
                cursor_y,
            )


    @staticmethod
    def _friendly_error(exc: Exception) -> str:
        if isinstance(exc, OllamaError):
            return str(exc)

        return f"Ошибка: {exc}"


    @Slot(int, str, int, int, object, object)
    def _on_done(
        self,
        request_id: int,
        text: str,
        x: int,
        y: int,
        source_rect,
        focus_rect,
    ) -> None:
        if request_id != self._request_id:
            return

        self._busy = False


        self.hud.show_message(
            text,
            (x, y),
            source_rect,
            focus_rect,
        )


    @Slot(int, str, int, int)
    def _on_failed(
        self,
        request_id: int,
        text: str,
        x: int,
        y: int,
    ) -> None:
        if request_id != self._request_id:
            return

        self._busy = False

        self.hud.show_message(
            text,
            (x, y),
        )


    def shutdown(self) -> None:
        self.pool.shutdown(
            wait=True,
            cancel_futures=True,
        )

        self.pipeline.close()

def ensure_ollama_running() -> None:
    host = "127.0.0.1"
    port = 11434

    def server_is_ready() -> bool:
        try:
            with socket.create_connection(
                (host, port),
                timeout=0.2,
            ):
                return True

        except OSError:
            return False

    if server_is_ready():
        return

        ollama_exe = os.path.join(
            os.environ["LOCALAPPDATA"],
            "Programs",
            "Ollama",
            "ollama.exe",
        )
    subprocess.Popen(
        [
            ollama_exe,
            "serve",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    deadline = time.perf_counter() + 10.0

    while time.perf_counter() < deadline:
        if server_is_ready():
            return

        time.sleep(0.1)

    raise RuntimeError(
        "Ollama server did not start within 10 seconds"
    )

def acquire_single_instance_mutex():
    kernel32 = ctypes.WinDLL(
        "kernel32",
        use_last_error=True,
    )

    kernel32.CreateMutexW.argtypes = [
        ctypes.c_void_p,
        ctypes.c_bool,
        ctypes.c_wchar_p,
    ]

    kernel32.CreateMutexW.restype = ctypes.c_void_p

    kernel32.CloseHandle.argtypes = [
        ctypes.c_void_p,
    ]

    kernel32.CloseHandle.restype = ctypes.c_bool

    mutex = kernel32.CreateMutexW(
        None,
        False,
        "Local\\LocalScreenTranslator.SingleInstance",
    )

    if not mutex:
        raise OSError(
            ctypes.get_last_error(),
            "Could not create single-instance mutex",
        )

    already_running = (
        ctypes.get_last_error() == 183
    )

    if already_running:
        kernel32.CloseHandle(
            mutex
        )
        return None

    return (
        kernel32,
        mutex,
    )

def main() -> int:
    enable_per_monitor_dpi_awareness()

    mutex_data = acquire_single_instance_mutex()

    if mutex_data is None:
        return 0

    kernel32, mutex = mutex_data

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    hud = TranslationHUD()

    try:
        ensure_ollama_running()

        controller = TranslatorController(hud)

    except Exception as exc:
        hud.show_message(
            f"Ошибка запуска: {exc}"
        )
        return app.exec()

    hotkeys = GlobalHotkeys()

    hotkeys.triggered.connect(
        controller.trigger
    )

    hotkeys.error.connect(
        lambda message: hud.show_message(message)
    )

    hotkeys.start()

    tray = QSystemTrayIcon()

    tray.setIcon(
        app.style().standardIcon(
            QStyle.StandardPixmap.SP_ComputerIcon
        )
    )

    tray.setToolTip(
        "Local Screen Translator"
    )

    tray_menu = QMenu()

    settings_action = QAction(
        "Settings...",
        tray
    )

    tray_menu.addAction(
        settings_action
    )
    def open_settings() -> None:
        dialog = SettingsDialog()

        dialog.settings_saved.connect(
            hotkeys.restart
        )

        dialog.exec()

    settings_action.triggered.connect(
        open_settings
    )

    tray_menu.addSeparator()

    exit_action = QAction(
        "Exit",
        tray
    )

    tray_menu.addAction(
        exit_action
    )

    tray.setContextMenu(
        tray_menu
    )

    exit_action.triggered.connect(
        app.quit
    )

    tray.show()

    if not USER_SETTINGS.first_run_completed:
        QTimer.singleShot(
            0,
            open_settings,
        )

    def cleanup() -> None:
        tray.hide()

        hotkeys.stop()

        controller.shutdown()

        ollama_exe = os.path.join(
            os.environ["LOCALAPPDATA"],
            "Programs",
            "Ollama",
            "ollama.exe",
        )

        for model_name in (
            "qwen3:4b",
            "riva-translate",
        ):
            try:
                subprocess.run(
                    [
                        ollama_exe,
                        "stop",
                        model_name,
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    timeout=5,
                    check=False,
                )

            except Exception:
                pass

        # Полностью закрываем Ollama server.
        # ollama stop выгружает модели, но сам сервер не завершает.
        try:
            subprocess.run(
                [
                    "taskkill",
                    "/F",
                    "/T",
                    "/IM",
                    "ollama.exe",
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW,
                timeout=5,
                check=False,
            )

        except Exception:
            pass
        try:
            subprocess.run(
                [
                    "taskkill",
                    "/F",
                    "/T",
                    "/IM",
                    "ollama app.exe",
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW,
                timeout=5,
                check=False,
            )

        except Exception:
            pass
        # Страховка на случай оставшегося model runner.
        try:
            subprocess.run(
                [
                    "taskkill",
                    "/F",
                    "/T",
                    "/IM",
                    "llama-server.exe",
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW,
                timeout=5,
                check=False,
            )

        except Exception:
            pass

    app.aboutToQuit.connect(
        cleanup
    )

    try:
        return app.exec()

    finally:
        kernel32.CloseHandle(
            mutex
        )


if __name__ == "__main__":
    raise SystemExit(main())