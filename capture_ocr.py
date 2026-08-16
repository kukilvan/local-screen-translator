from __future__ import annotations
import os
import sys

os.environ["FLAGS_enable_pir_api"] = "0"

_NVIDIA_DLL_HANDLES = []


def _add_nvidia_dll_directories() -> None:
    """
    Add CUDA/cuDNN DLL directories for both development venv and
    PyInstaller onedir layouts.
    """
    nvidia_roots = []

    nvidia_roots.append(
        os.path.join(
            sys.prefix,
            "Lib",
            "site-packages",
            "nvidia",
        )
    )

    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        nvidia_roots.append(
            os.path.join(meipass, "nvidia")
        )

    exe_dir = os.path.dirname(
        os.path.abspath(sys.executable)
    )
    nvidia_roots.extend(
        [
            os.path.join(exe_dir, "i", "nvidia"),
            os.path.join(exe_dir, "_internal", "nvidia"),
        ]
    )

    seen_roots = set()
    dll_dirs = []

    for nvidia_root in nvidia_roots:
        key = os.path.normcase(
            os.path.abspath(nvidia_root)
        )
        if key in seen_roots:
            continue
        seen_roots.add(key)

        if not os.path.isdir(nvidia_root):
            continue

        cuda_bin = os.path.join(
            nvidia_root,
            "cu13",
            "bin",
            "x86_64",
        )
        if os.path.isdir(cuda_bin):
            dll_dirs.append(cuda_bin)

        cudnn_root = os.path.join(
            nvidia_root,
            "cudnn",
        )

        if os.path.isdir(cudnn_root):
            for root, _, files in os.walk(cudnn_root):
                if "cudnn64_9.dll" in files:
                    dll_dirs.append(root)
                    break

    seen_dirs = set()

    for dll_dir in dll_dirs:
        key = os.path.normcase(
            os.path.abspath(dll_dir)
        )
        if key in seen_dirs:
            continue
        seen_dirs.add(key)

        _NVIDIA_DLL_HANDLES.append(
            os.add_dll_directory(dll_dir)
        )

        os.environ["PATH"] = (
            dll_dir
            + os.pathsep
            + os.environ.get("PATH", "")
        )


_add_nvidia_dll_directories()

import re
import time
import ctypes
import ctypes.wintypes as wintypes
from dataclasses import dataclass
from math import hypot
from statistics import median
from typing import Iterable
from paddleocr import PaddleOCR


import cv2
import dxcam
import numpy as np

from config import SETTINGS
from runtime_paths import PADDLE_DET_MODEL_DIR, PADDLE_REC_MODEL_DIR


@dataclass(frozen=True)
class Rect:
    x: float
    y: float
    w: float
    h: float

    @property
    def left(self) -> float:
        return self.x

    @property
    def top(self) -> float:
        return self.y

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    def contains(self, x: float, y: float, padding: float = 0.0) -> bool:
        return (
            self.left - padding <= x <= self.right + padding
            and self.top - padding <= y <= self.bottom + padding
        )


@dataclass(frozen=True)
class WordBox:
    text: str
    rect: Rect


@dataclass(frozen=True)
class LineBox:
    text: str
    rect: Rect
    words: tuple[WordBox, ...]


@dataclass(frozen=True)
class OCRSnapshot:
    text: str
    words: tuple[WordBox, ...]
    lines: tuple[LineBox, ...]
    cursor_x: float
    cursor_y: float


def _distance_to_rect(x: float, y: float, r: Rect) -> float:
    dx = max(r.left - x, 0.0, x - r.right)
    dy = max(r.top - y, 0.0, y - r.bottom)
    return hypot(dx, dy)


def _union_rect(rects: Iterable[Rect]) -> Rect:
    rects = tuple(rects)
    left = min(r.left for r in rects)
    top = min(r.top for r in rects)
    right = max(r.right for r in rects)
    bottom = max(r.bottom for r in rects)
    return Rect(left, top, right - left, bottom - top)





class ScreenOCR:
    """
    One-shot DXGI capture + Windows.Media.Ocr.

    Important: we deliberately do NOT call camera.start(). That means there is
    no 60/120/240 FPS capture thread running in the background. Capture occurs
    only when a hotkey is pressed.
    """

    def __init__(self) -> None:

        for model_dir, label in (
            (PADDLE_DET_MODEL_DIR, "Paddle detection model"),
            (PADDLE_REC_MODEL_DIR, "Paddle recognition model"),
        ):
            if not model_dir.is_dir():
                raise RuntimeError(
                    "LST-FILE-001: "
                    f"{label} not found: {model_dir}"
                )

        self.paddle = PaddleOCR(
            text_detection_model_name="PP-OCRv6_small_det",
            text_detection_model_dir=str(PADDLE_DET_MODEL_DIR),
            text_recognition_model_name="latin_PP-OCRv5_mobile_rec",
            text_recognition_model_dir=str(PADDLE_REC_MODEL_DIR),
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            enable_mkldnn=False,
            return_word_box=True,
            device="gpu:0",
            engine="paddle",
        )

        self.camera = dxcam.create(
            device_idx=SETTINGS.capture_device_idx,
            output_idx=SETTINGS.capture_output_idx,
            output_color="BGRA",
            backend=SETTINGS.capture_backend,
            processor_backend="numpy",
        )

    @staticmethod
    def cursor_pos() -> tuple[int, int]:
        point = wintypes.POINT()
        if not ctypes.windll.user32.GetCursorPos(ctypes.byref(point)):
            raise ctypes.WinError()
        return int(point.x), int(point.y)

    def _output_geometry(self) -> tuple[int, int, int, int]:
        # DXcam 0.3.x exposes the selected DXGI output through _output.
        # We use its native DesktopCoordinates so multi-monitor origins,
        # including negative X/Y, are handled correctly.
        desc = self.camera._output.desc  # type: ignore[attr-defined]
        if desc is None:
            self.camera._output.update_desc()  # type: ignore[attr-defined]
            desc = self.camera._output.desc  # type: ignore[attr-defined]
        desktop = desc.DesktopCoordinates
        left = int(desktop.left)
        top = int(desktop.top)
        right = int(desktop.right)
        bottom = int(desktop.bottom)
        return left, top, right, bottom

    def _capture_around_cursor(
        self,
        roi_width: int,
        roi_height: int,
        cursor_global: tuple[int, int] | None = None,
    ) -> tuple[np.ndarray, tuple[float, float]]:
        cursor_gx, cursor_gy = cursor_global or self.cursor_pos()
        out_left, out_top, out_right, out_bottom = self._output_geometry()

        if not (
            out_left <= cursor_gx < out_right
            and out_top <= cursor_gy < out_bottom
        ):
            raise RuntimeError(
                "LST-CAP-001: Cursor is outside the monitor currently "
                "captured by DXcam. Check capture_device_idx / "
                "capture_output_idx in config.py."
            )

        out_w = out_right - out_left
        out_h = out_bottom - out_top
        cx = cursor_gx - out_left
        cy = cursor_gy - out_top

        width = min(roi_width, out_w)
        height = min(roi_height, out_h)

        left = int(round(cx - width / 2))
        top = int(round(cy - height / 2))
        left = max(0, min(left, out_w - width))
        top = max(0, min(top, out_h - height))
        right = left + width
        bottom = top + height

                # Не используем старый закэшированный кадр после простоя.
        # Ждём именно свежий кадр от Desktop Duplication.
        frame = None
        deadline = time.perf_counter() + 0.12

        while frame is None and time.perf_counter() < deadline:
            frame = self.camera.grab(
                region=(left, top, right, bottom),
                new_frame_only=True,
            )

            if frame is None:
                time.sleep(0.005)

        if frame is None:
            raise RuntimeError(
                "LST-CAP-001: DXcam did not receive a fresh frame from the screen."
            )

        cursor_local = (float(cx - left), float(cy - top))
        return frame, cursor_local

    def _recognize(
        self,
        frame_bgra: np.ndarray,
        cursor_local: tuple[float, float],
        det_limit_side_len: int = 960,
    ) -> OCRSnapshot:
        scale = max(1.0, float(SETTINGS.ocr_scale))
        frame_h = float(frame_bgra.shape[0])

        # DXcam gives us BGRA. PaddleOCR expects a normal 3-channel image.
        # The first three DXcam channels are already BGR.
        bgr = np.ascontiguousarray(frame_bgra[:, :, :3])

        if scale != 1.0:
            bgr = cv2.resize(
                bgr,
                None,
                fx=scale,
                fy=scale,
                interpolation=cv2.INTER_CUBIC,
            )

        results = self.paddle.predict(
            bgr,
            text_det_limit_side_len=det_limit_side_len,
            text_det_limit_type="max",
        )

        words: list[WordBox] = []
        lines: list[LineBox] = []
        full_text: list[str] = []

        def rect_from_region(region) -> Rect:
            points = np.asarray(region, dtype=np.float32).reshape(-1, 2)

            left = float(points[:, 0].min()) / scale
            top = float(points[:, 1].min()) / scale
            right = float(points[:, 0].max()) / scale
            bottom = float(points[:, 1].max()) / scale

            return Rect(
                left,
                top,
                right - left,
                bottom - top,
            )

        for result in results:
            rec_texts = list(result.get("rec_texts", []))
            rec_polys = list(result.get("rec_polys", []))
            text_words = list(result.get("text_word", []))
            text_word_regions = list(result.get("text_word_region", []))

            for line_index, line_text in enumerate(rec_texts):
                line_text = str(line_text).strip()

                if not line_text:
                    continue

                # Ignore OCR lines clipped by the top/bottom edge of the ROI.
                # Partial glyphs near the crop boundary often become garbage.
                if line_index < len(rec_polys):
                    edge_rect = rect_from_region(rec_polys[line_index])
                    edge_margin = max(6.0, edge_rect.h * 0.45)

                    if (
                        edge_rect.top <= edge_margin
                        or edge_rect.bottom >= frame_h - edge_margin
                    ):
                        continue
                full_text.append(line_text)
                line_words: list[WordBox] = []

                if (
                    line_index < len(text_words)
                    and line_index < len(text_word_regions)
                ):
                    tokens = text_words[line_index]
                    regions = text_word_regions[line_index]

                    current_text = ""
                    current_rects: list[Rect] = []

                    def flush_word() -> None:
                        nonlocal current_text, current_rects

                        raw_text = current_text.strip()

                        if not raw_text or not current_rects:
                            current_text = ""
                            current_rects = []
                            return

                        word_rect = _union_rect(current_rects)

                        matches = list(
                            re.finditer(
                                r"\w+(?:['’-]\w+)*",
                                raw_text,
                                re.UNICODE,
                            )
                        )

                        if not matches:
                            current_text = ""
                            current_rects = []
                            return

                        if len(matches) == 1:
                            cleaned = matches[0].group(0)

                            wb = WordBox(
                                cleaned,
                                word_rect,
                            )

                            line_words.append(wb)
                            words.append(wb)

                        else:
                            text_length = max(
                                1,
                                len(raw_text),
                            )

                            for match in matches:
                                cleaned = match.group(0)

                                left_ratio = (
                                    match.start()
                                    / text_length
                                )

                                right_ratio = (
                                    match.end()
                                    / text_length
                                )

                                sub_left = (
                                    word_rect.left
                                    + word_rect.w * left_ratio
                                )

                                sub_right = (
                                    word_rect.left
                                    + word_rect.w * right_ratio
                                )

                                sub_rect = Rect(
                                    sub_left,
                                    word_rect.top,
                                    max(
                                        1.0,
                                        sub_right - sub_left,
                                    ),
                                    word_rect.h,
                                )

                                wb = WordBox(
                                    cleaned,
                                    sub_rect,
                                )

                                line_words.append(wb)
                                words.append(wb)

                        current_text = ""
                        current_rects = []

                    for token, region in zip(tokens, regions):
                        token = str(token)

                        if not token:
                            continue

                        # A leading space means a new word begins here.
                        if token[0].isspace():
                            flush_word()

                        core = token.strip()

                        if core:
                            current_text += core
                            current_rects.append(rect_from_region(region))

                        # A trailing space means the current word has ended.
                        if token[-1].isspace():
                            flush_word()

                    flush_word()

                # Prefer Paddle's detected line polygon for the complete line.
                if line_index < len(rec_polys):
                    line_rect = rect_from_region(rec_polys[line_index])
                elif line_words:
                    line_rect = _union_rect(w.rect for w in line_words)
                else:
                    continue

                lines.append(
                    LineBox(
                        text=line_text,
                        rect=line_rect,
                        words=tuple(line_words),
                    )
                )

        text = "\n".join(full_text).strip()

        if not text:
            debug_path = "debug_ocr_empty.png"

            cv2.imwrite(
                debug_path,
                bgr,
            )

            raw_texts = []

            for debug_result in results:
                raw_texts.extend(
                    str(x)
                    for x in debug_result.get(
                        "rec_texts",
                        [],
                    )
                )

            print(
                "OCR EMPTY DEBUG | "
                f"raw_rec_texts={raw_texts!r} | "
                f"frame_shape={bgr.shape!r} | "
                f"saved={debug_path}",
                flush=True,
            )

            raise RuntimeError(
                "PaddleOCR found no text near the cursor."
            )

        return OCRSnapshot(
            text=text,
            words=tuple(words),
            lines=tuple(lines),
            cursor_x=cursor_local[0],
            cursor_y=cursor_local[1],
        )

    def snapshot_word_region(
        self, cursor_global: tuple[int, int] | None = None
    ) -> OCRSnapshot:


        frame, cursor = self._capture_around_cursor(
            SETTINGS.word_roi_width,
            SETTINGS.word_roi_height,
            cursor_global=cursor_global,
        )



        snapshot = self._recognize(
            frame,
            cursor,
            det_limit_side_len=960,
        )





        return snapshot

    def snapshot_paragraph_region(
        self, cursor_global: tuple[int, int] | None = None
    ) -> OCRSnapshot:


        frame, cursor = self._capture_around_cursor(
            SETTINGS.paragraph_roi_width,
            SETTINGS.paragraph_roi_height,
            cursor_global=cursor_global,
        )



        snapshot = self._recognize(
            frame,
            cursor,
            det_limit_side_len=1536,
        )





        return snapshot


def choose_word(snapshot: OCRSnapshot) -> WordBox:
    if not snapshot.words:
        raise RuntimeError("OCR found no text near the cursor.")

    x, y = snapshot.cursor_x, snapshot.cursor_y

    # Если курсор реально находится на слове или совсем рядом — берем его сразу.
    direct = [w for w in snapshot.words if w.rect.contains(x, y, padding=8.0)]
    if direct:
        return min(direct, key=lambda w: hypot(w.rect.cx - x, w.rect.cy - y))

    # Подстраиваем допуск под размер текста.
    heights = [line.rect.h for line in snapshot.lines if line.rect.h > 0]
    typical_h = float(median(heights)) if heights else 24.0
    vertical_limit = max(
        30.0,
        min(float(SETTINGS.max_word_distance_px), typical_h * 2.8),
    )

    # Приоритет слову, на которое указывает кончик курсора снизу.
    # Это делает естественный жест "поставить стрелку под словом"
    # гораздо надежнее, особенно между двумя строками текста.
    upward_candidates = []
    upward_limit = max(18.0, min(vertical_limit, typical_h * 1.6))

    for w in snapshot.words:
        # Рассматриваем только слова ВЫШЕ кончика курсора.
        if w.rect.bottom > y:
            continue

        vgap = y - w.rect.bottom
        if vgap > upward_limit:
            continue

        # Немного расширяем слово влево/вправо,
        # чтобы не требовалось идеально попадать по центру.
        x_padding = max(8.0, min(18.0, w.rect.w * 0.25))

        if not (w.rect.left - x_padding <= x <= w.rect.right + x_padding):
            continue

        if w.rect.left <= x <= w.rect.right:
            hgap = 0.0
        else:
            hgap = min(abs(x - w.rect.left), abs(x - w.rect.right))

        score = (
            vgap
            + hgap * 1.8
            + abs(w.rect.cx - x) * 0.05
        )

        upward_candidates.append((score, w))

    if upward_candidates:
        return min(upward_candidates, key=lambda item: item[0])[1]	

    def vertical_gap(r: Rect) -> float:
        if r.top <= y <= r.bottom:
            return 0.0
        if y > r.bottom:
            return y - r.bottom
        return r.top - y

    def horizontal_gap(r: Rect) -> float:
        return max(r.left - x, 0.0, x - r.right)

    # Сначала определяем строку.
    # Строке чуть ВЫШЕ курсора даем преимущество:
    # так можно ставить стрелку под словом, а не прямо на буквы.
    line_candidates = []

    for line in snapshot.lines:
        if not line.words:
            continue

        vgap = vertical_gap(line.rect)

        if vgap > vertical_limit:
            continue

        hgap = horizontal_gap(line.rect)

        if hgap > float(SETTINGS.max_word_distance_px) * 1.5:
            continue

        if line.rect.bottom <= y:
            vertical_score = vgap * 0.65
        elif line.rect.top > y:
            vertical_score = vgap * 1.15
        else:
            vertical_score = 0.0

        score = vertical_score + hgap * 0.20
        line_candidates.append((score, line))

    if line_candidates:
        _, line = min(line_candidates, key=lambda item: item[0])

        # Когда строка определена, выбираем слово в основном по X.
        # Поэтому курсор может быть под словом или между словами.
        target = min(
            line.words,
            key=lambda w: (
                horizontal_gap(w.rect),
                abs(w.rect.cx - x),
            ),
        )

        if horizontal_gap(target.rect) <= float(SETTINGS.max_word_distance_px):
            return target

    # Запасной вариант для необычной разметки OCR.
    nearest = min(
        snapshot.words,
        key=lambda w: _distance_to_rect(x, y, w.rect),
    )

    if _distance_to_rect(x, y, nearest.rect) > float(SETTINGS.max_word_distance_px):
        raise RuntimeError("No OCR word was found near the cursor.")

    return nearest


def context_for_word(snapshot: OCRSnapshot, target: WordBox) -> str:
    """
    Keep the OCR context compact but meaningful:
    target line plus up to four neighboring lines on each side.
    """
    if not snapshot.lines:
        return snapshot.text[:2500]

    target_index = min(
        range(len(snapshot.lines)),
        key=lambda i: _distance_to_rect(target.rect.cx, target.rect.cy, snapshot.lines[i].rect),
    )
    lo = max(0, target_index - 4)
    hi = min(len(snapshot.lines), target_index + 5)
    text = "\n".join(line.text for line in snapshot.lines[lo:hi]).strip()
    return text[:2500] if text else snapshot.text[:2500]


def _horizontal_relation(a: Rect, b: Rect) -> bool:
    overlap = max(0.0, min(a.right, b.right) - max(a.left, b.left))
    min_width = max(1.0, min(a.w, b.w))
    overlap_ratio = overlap / min_width
    left_delta = abs(a.left - b.left)

    # Dialogue/subtitle lines can be centered and have different widths.
    return overlap_ratio >= 0.12 or left_delta <= 260.0


def choose_paragraph(
    snapshot: OCRSnapshot,
    return_rect: bool = False,
):
    """
    Collect only the connected visual text block around the cursor.
    Keep PaddleOCR punctuation intact and let the LLM decide sentence boundaries.
    """

    if not snapshot.lines:
        if snapshot.text:
            return f"<<<CURSOR>>> {snapshot.text}"[:5000]
        raise RuntimeError("OCR found no text to translate.")

    target = choose_word(snapshot)

    lines = list(snapshot.lines)

    anchor_index = min(
        range(len(lines)),
        key=lambda i: _distance_to_rect(
            target.rect.cx,
            target.rect.cy,
            lines[i].rect,
        ),
    )

    anchor = lines[anchor_index]

    heights = [line.rect.h for line in lines if line.rect.h > 2]
    typical_h = float(median(heights)) if heights else 24.0

    max_vertical_gap = max(28.0, typical_h * 1.8)

    max_center_gap = max(
        36.0,
        typical_h * 2.6,
    )

    def same_text_block(
        a: LineBox,
        b: LineBox,
    ) -> bool:
        # Paddle может немного менять высоту одной и той же
        # строки между соседними захватами.
        taller = max(
            a.rect.h,
            b.rect.h,
            1.0,
        )

        size_ratio = (
            min(a.rect.h, b.rect.h)
            / taller
        )

        if size_ratio < 0.50:
            return False

        overlap = max(
            0.0,
            min(a.rect.right, b.rect.right)
            - max(a.rect.left, b.rect.left),
        )

        overlap_ratio = overlap / max(
            1.0,
            min(a.rect.w, b.rect.w),
        )

        left_delta = abs(
            a.rect.left - b.rect.left
        )

        center_delta = abs(
            a.rect.cx - b.rect.cx
        )

        return (
            overlap_ratio >= 0.35
            or left_delta <= max(
                70.0,
                typical_h * 3.0,
            )
            or center_delta <= max(
                110.0,
                typical_h * 5.0,
            )
        )

    selected = {anchor_index}

    # Grow upward inside the same visual column/block.
    current = anchor

    for _ in range(4):
        candidates = []

        for i, line in enumerate(lines):
            if i in selected:
                continue

            # Строка должна находиться выше по центру.
# Небольшое перекрытие bounding box между соседними строками допустимо.
            if line.rect.cy >= current.rect.cy:
              continue

            center_gap = (
                current.rect.cy
                - line.rect.cy
            )

            if center_gap > max_center_gap:
                continue

            if not same_text_block(line, current):
                continue

            candidates.append(
                (
                    center_gap,
                    abs(
                        line.rect.cx
                        - current.rect.cx
                    ),
                    i,
                )
            )

        if not candidates:
            break

        _, _, i = min(candidates)
        selected.add(i)
        current = lines[i]

    # Grow downward inside the same visual column/block.
    current = anchor

    for _ in range(4):
        candidates = []

        for i, line in enumerate(lines):
            if i in selected:
                continue

            # Строка должна находиться ниже по центру.
# Paddle может давать соседним строкам слегка перекрывающиеся рамки.
            if line.rect.cy <= current.rect.cy:
              continue

            center_gap = (
                line.rect.cy
                - current.rect.cy
            )

            if center_gap > max_center_gap:
                continue

            if not same_text_block(current, line):
                continue

            candidates.append((center_gap, abs(line.rect.cx - current.rect.cx), i))

        if not candidates:
            break

        _, _, i = min(candidates)
        selected.add(i)
        current = lines[i]

    chosen_lines = sorted(
        (lines[i] for i in selected),
        key=lambda line: (line.rect.top, line.rect.left),
    )

    output_lines: list[str] = []
    used_lines: list[LineBox] = []

    for line in chosen_lines:
        line_text = line.text.strip()

        if not line_text:
            continue

        # Убираем OCR-мусор вроде ":", ".", "+ +", "□", "×".
        # Нормальная строка должна содержать хотя бы букву или цифру.
        if not any(char.isalnum() for char in line_text):
            continue

        if line is anchor:
            marker_pos = None
            search_from = 0

            for word in line.words:
                wt = word.text.strip()

                if not wt:
                    continue

                pos = line_text.lower().find(
                    wt.lower(),
                    search_from,
                )

                if word is target:
                    if pos >= 0:
                        marker_pos = pos
                    break

                if pos >= 0:
                    search_from = pos + len(wt)

            if marker_pos is None:
                pos = line_text.lower().find(target.text.lower())
                marker_pos = pos if pos >= 0 else 0

            line_text = (
                line_text[:marker_pos]
                + "<<<CURSOR>>> "
                + line_text[marker_pos:]
            )

        output_lines.append(line_text)
        used_lines.append(line)

    result = "\n".join(output_lines).strip()

    if not result:
        raise RuntimeError(
            "Could not build a text block near the cursor."
        )

    if return_rect:
        paragraph_rect = _union_rect(
            [
                line.rect
                for line in used_lines
            ]
        )

        return (
            result[:5000],
            paragraph_rect,
        )

    return result[:5000]
