from __future__ import annotations
import traceback
import ctypes
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor

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
    """
    Surround the full SimAlign target span with HUD markers.

    Example:
        Она пожала плечами.
            ↓
        Она <<<CURSOR>>>пожала плечами<<<END_CURSOR>>>.
    """
    if not token_indices:
        return text

    matches = list(TOKEN_RE.finditer(text))

    start_index = min(token_indices)
    end_index = max(token_indices)

    if (
        start_index < 0
        or end_index >= len(matches)
    ):
        return text

    start_pos = matches[start_index].start()
    end_pos = matches[end_index].end()

    return (
        text[:start_pos]
        + CURSOR_MARKER
        + text[start_pos:end_pos]
        + CURSOR_END_MARKER
        + text[end_pos:]
    )


class WorkerSignals(QObject):
    done = Signal(int, str, int, int)
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

                        print(
                            "WORD CURSOR LOCAL:",
                            f"x={snapshot.cursor_x:.1f}",
                            f"y={snapshot.cursor_y:.1f}",
                            flush=True,
                        )

                        print(
                            "WORD NEAR BOXES:",
                            flush=True,
                        )

                        for debug_word in snapshot.words:
                            if (
                                abs(debug_word.rect.cx - snapshot.cursor_x) <= 160
                                and abs(debug_word.rect.cy - snapshot.cursor_y) <= 80
                            ):
                                print(
                                    f"  {debug_word.text!r} | "
                                    f"x={debug_word.rect.x:.1f} "
                                    f"y={debug_word.rect.y:.1f} "
                                    f"w={debug_word.rect.w:.1f} "
                                    f"h={debug_word.rect.h:.1f} "
                                    f"cx={debug_word.rect.cx:.1f} "
                                    f"cy={debug_word.rect.cy:.1f}",
                                    flush=True,
                                )

                        target = choose_word(snapshot)

                        print(
                            "WORD CHOSEN:",
                            repr(target.text),
                            flush=True,
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

                print(
                    "WORD SOURCE:",
                    repr(context),
                    flush=True,
                )

                print(
                    "WORD TARGET:",
                    repr(target.text),
                    flush=True,
                )

                print(
                    "WORD SENTENCE RIVA:",
                    repr(sentence_translation),
                    flush=True,
                )

                print(
                    "WORD EXPRESSION:",
                    repr(source_span),
                    flush=True,
                )

                print(
                    "WORD DICTIONARY:",
                    repr(dictionary_translation),
                    flush=True,
                )

                print(
                    "WORD LOGIC USED:",
                    logic_used,
                    flush=True,
                )

                print(
                    f"WORD TIMING: "
                    f"OCR={t1 - t0:.3f}s | "
                    f"prepare={t2 - t1:.3f}s | "
                    f"Riva={t3 - t2:.3f}s | "
                    f"Logic={t4 - t3:.3f}s | "
                    f"TOTAL={t4 - t0:.3f}s",
                    flush=True,
                )
            elif mode == "paragraph":
                t0 = time.perf_counter()

                snapshot = self.ocr.snapshot_paragraph_region(
                    (cursor_x, cursor_y)
                )

                t1 = time.perf_counter()

                print(
                    "\nRAW OCR LINES:",
                    flush=True,
                )

                for i, line in enumerate(snapshot.lines):
                    print(
                        f"{i}: {line.text!r} | "
                        f"x={line.rect.x:.1f} "
                        f"y={line.rect.y:.1f} "
                        f"w={line.rect.w:.1f} "
                        f"h={line.rect.h:.1f}",
                        flush=True,
                    )

                print(
                    "",
                    flush=True,
                )

                marked_paragraph = choose_paragraph(
                    snapshot
                )

                t2 = time.perf_counter()

                (
                    paragraph,
                    target_word,
                    target_occurrence,
                ) = extract_cursor_word(
                    marked_paragraph
                )

                print(
                    "PARAGRAPH SOURCE:",
                    repr(paragraph),
                    flush=True,
                )

                print(
                    "CURSOR WORD:",
                    repr(target_word),
                    flush=True,
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

                print(
                    "RIVA TRANSLATION:",
                    repr(translated),
                    flush=True,
                )

                print(
                    "SIMALIGN:",
                    repr(target_word),
                    "->",
                    repr(target_phrase),
                    "indices=",
                    target_indices,
                    flush=True,
                )

                if target_indices:
                    translated = insert_cursor_markers_by_token_indices(
                        translated,
                        target_indices,
                    )

                t5 = time.perf_counter()

                print(
                    f"TIMING: "
                    f"capture+OCR={t1 - t0:.3f}s | "
                    f"choose={t2 - t1:.3f}s | "
                    f"marker_parse={t3 - t2:.3f}s | "
                    f"Riva+SimAlign={t4 - t3:.3f}s | "
                    f"prepare_HUD={t5 - t4:.3f}s | "
                    f"TOTAL={t5 - t0:.3f}s",
                    flush=True,
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


    @Slot(int, str, int, int)
    def _on_done(
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
        self.pipeline.close()

        self.pool.shutdown(
            wait=False,
            cancel_futures=True,
        )


def main() -> int:
    enable_per_monitor_dpi_awareness()

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    hud = TranslationHUD()

    try:
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

    def cleanup() -> None:
        hotkeys.stop()
        controller.shutdown()

    app.aboutToQuit.connect(cleanup)

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())