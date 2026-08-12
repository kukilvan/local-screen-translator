from __future__ import annotations
import html
import re
import ctypes

from PySide6.QtCore import QPoint, QRect, Qt, QTimer
from PySide6.QtGui import QCursor, QGuiApplication
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget

from config import SETTINGS


class TranslationHUD(QWidget):
    def __init__(self) -> None:
        flags = (
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.WindowDoesNotAcceptFocus
            | Qt.WindowType.WindowTransparentForInput
        )
        super().__init__(None, flags)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)

        self._label = QLabel()
        self._label.setWordWrap(True)
        self._label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self._label.setStyleSheet(
            """
            QLabel {
                color: rgba(255, 255, 255, 245);
                font-family: "Segoe UI";
                font-size: 15px;
                font-weight: 500;
                padding: 14px 16px;
            }
            """
        )

        frame = QFrame()
        frame.setObjectName("HudFrame")
        frame.setStyleSheet(
            """
            QFrame#HudFrame {
                background-color: rgba(20, 22, 27, 232);
                border: 1px solid rgba(255, 255, 255, 42);
                border-radius: 12px;
            }
            """
        )
        frame_layout = QVBoxLayout(frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.addWidget(self._label)

        root = QVBoxLayout(self)
        root.setContentsMargins(8, 8, 8, 8)
        root.addWidget(frame)

        self._auto_hide = QTimer(self)
        self._auto_hide.setSingleShot(True)
        self._auto_hide.timeout.connect(self.hide)

        # While visible only, check mouse buttons. The HUD itself is click-through,
        # so the game/app receives the click and the popup disappears immediately.
        self._click_watch = QTimer(self)
        self._click_watch.setInterval(35)
        self._click_watch.timeout.connect(self._hide_on_mouse_click)

        self._mouse_was_down = False

    def _apply_win32_noactivate(self) -> None:
        if not self.winId():
            return

        hwnd = int(self.winId())
        GWL_EXSTYLE = -20
        WS_EX_NOACTIVATE = 0x08000000
        WS_EX_TOOLWINDOW = 0x00000080
        WS_EX_TRANSPARENT = 0x00000020
        HWND_TOPMOST = -1
        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        SWP_NOACTIVATE = 0x0010

        user32 = ctypes.windll.user32

        get_window_long = user32.GetWindowLongPtrW
        set_window_long = user32.SetWindowLongPtrW
        get_window_long.restype = ctypes.c_longlong
        set_window_long.restype = ctypes.c_longlong

        exstyle = get_window_long(hwnd, GWL_EXSTYLE)
        set_window_long(
            hwnd,
            GWL_EXSTYLE,
            exstyle | WS_EX_NOACTIVATE | WS_EX_TOOLWINDOW | WS_EX_TRANSPARENT,
        )

        user32.SetWindowPos(
            hwnd,
            HWND_TOPMOST,
            0,
            0,
            0,
            0,
            SWP_NOSIZE | SWP_NOMOVE | SWP_NOACTIVATE,
        )

    @staticmethod
    def _any_mouse_button_down() -> bool:
        user32 = ctypes.windll.user32
        VK_LBUTTON = 0x01
        VK_RBUTTON = 0x02
        VK_MBUTTON = 0x04
        return any(
            user32.GetAsyncKeyState(vk) & 0x8000
            for vk in (VK_LBUTTON, VK_RBUTTON, VK_MBUTTON)
        )

    def _hide_on_mouse_click(self) -> None:
        down = self._any_mouse_button_down()
        if down and not self._mouse_was_down:
            self.hide()
        self._mouse_was_down = down

    def hideEvent(self, event) -> None:
        self._auto_hide.stop()
        self._click_watch.stop()
        super().hideEvent(event)

    def show_message(
        self,
        text: str,
        cursor_pos: tuple[int, int] | None = None,
    ) -> None:
        raw_text = text.strip()

        start_marker = "<<<CURSOR>>>"
        end_marker = "<<<END_CURSOR>>>"

        start_pos = raw_text.find(start_marker)

        if start_pos >= 0:
            before_text = raw_text[:start_pos]

            after_start = raw_text[
                start_pos + len(start_marker):
            ]

            end_pos = after_start.find(end_marker)

            if end_pos >= 0:
                highlighted_text = after_start[:end_pos]

                rest_text = after_start[
                    end_pos + len(end_marker):
                ]

                display_text = (
                    html.escape(before_text)
                    + '<span style="color:#73D5FF; font-weight:700;">'
                    + html.escape(highlighted_text)
                    + "</span>"
                    + html.escape(rest_text)
                )

            else:
                # Совместимость со старым одиночным маркером.
                match = re.match(
                    r"(\s*)([^\s,.;:!?]+)(.*)",
                    after_start,
                    flags=re.DOTALL,
                )

                if match:
                    leading_space = match.group(1)
                    highlighted_word = match.group(2)
                    rest_text = match.group(3)

                    display_text = (
                        html.escape(before_text)
                        + html.escape(leading_space)
                        + '<span style="color:#73D5FF; font-weight:700;">'
                        + html.escape(highlighted_word)
                        + "</span>"
                        + html.escape(rest_text)
                    )
                else:
                    display_text = html.escape(
                        raw_text.replace(start_marker, "")
                    )

        else:
            display_text = html.escape(raw_text)

        # Служебные маркеры никогда не показываем пользователю.
        display_text = display_text.replace(
            html.escape(start_marker),
            "",
        )

        display_text = display_text.replace(
            html.escape(end_marker),
            "",
        )

        display_text = display_text.replace("\n", "<br>")

        self._label.setTextFormat(Qt.TextFormat.RichText)
        self._label.setText(display_text)

        plain_length = len(
            raw_text
            .replace(start_marker, "")
            .replace(end_marker, "")
        )

        if plain_length <= 80:
            clean_plain_text = (
                raw_text
                .replace(start_marker, "")
                .replace(end_marker, "")
            )

            lines = clean_plain_text.splitlines()

            if not lines:
                lines = [clean_plain_text]

            font_metrics = self._label.fontMetrics()

            longest_line_width = max(
                font_metrics.horizontalAdvance(line)
                for line in lines
            )

            content_width = max(
                180,
                min(
                    360,
                    longest_line_width + 40,
                ),
            )

        elif plain_length <= 220:
            content_width = 500

        else:
            content_width = 640

        self._label.setFixedWidth(
            content_width
        )

        self._label.adjustSize()
        self.adjustSize()
        

        if cursor_pos is None:
            cursor = QCursor.pos()
        else:
            cursor = QPoint(
                cursor_pos[0],
                cursor_pos[1],
            )

        screen = QGuiApplication.screenAt(cursor)

        if screen is None:
            screen = QGuiApplication.primaryScreen()

        if screen is None:
            self.show()
            return

        available: QRect = screen.availableGeometry()

        x = cursor.x() + SETTINGS.hud_offset_x
        y = cursor.y() + SETTINGS.hud_offset_y

        if x + self.width() > available.right():
            x = cursor.x() - self.width() - 18

        if y + self.height() > available.bottom():
            y = cursor.y() - self.height() - 18

        x = max(
            available.left(),
            min(
                x,
                available.right() - self.width() + 1,
            ),
        )

        y = max(
            available.top(),
            min(
                y,
                available.bottom() - self.height() + 1,
            ),
        )

        self.move(x, y)
        self.show()
        self._apply_win32_noactivate()

        self._mouse_was_down = self._any_mouse_button_down()
        self._click_watch.start()
        self._auto_hide.start(
            SETTINGS.hud_auto_hide_ms
        )
