from __future__ import annotations

import threading

from PySide6.QtCore import Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from system_check import (
    FAIL,
    PASS,
    WARN,
    format_report,
    run_deep_system_check,
)
from system_check_help import format_self_help_report


class SystemCheckDialog(QDialog):
    check_finished = Signal(object)

    def __init__(
        self,
        parent=None,
        *,
        auto_start: bool = True,
    ) -> None:
        super().__init__(parent)

        self._full_report = ""
        self._running = False
        self.check_completed = False
        self.has_fail = False

        self.setWindowTitle(
            "Local Screen Translator - System Check"
        )
        self.setMinimumSize(
            760,
            520,
        )

        root = QVBoxLayout(self)

        title = QLabel(
            "<b>System compatibility check</b>"
        )
        root.addWidget(title)

        description = QLabel(
            "Local Screen Translator will test the GPU, "
            "CUDA OCR, screen capture, local AI models, "
            "alignment component and Windows speech."
        )
        description.setWordWrap(True)
        root.addWidget(description)

        self.status_label = QLabel(
            "Ready to check."
        )
        self.status_label.setWordWrap(True)
        root.addWidget(
            self.status_label
        )

        self.progress = QProgressBar()
        self.progress.setRange(0, 1)
        self.progress.setValue(0)
        root.addWidget(
            self.progress
        )

        self.report_edit = QTextEdit()
        self.report_edit.setReadOnly(True)
        self.report_edit.setPlaceholderText(
            "System Check results will appear here."
        )
        root.addWidget(
            self.report_edit,
            1,
        )

        buttons = QHBoxLayout()

        self.run_button = QPushButton(
            "Run again"
        )
        self.copy_button = QPushButton(
            "Copy report"
        )
        self.close_button = QPushButton(
            "Close"
        )

        self.copy_button.setEnabled(False)

        buttons.addWidget(
            self.run_button
        )
        buttons.addWidget(
            self.copy_button
        )
        buttons.addStretch(1)
        buttons.addWidget(
            self.close_button
        )

        root.addLayout(buttons)

        self.run_button.clicked.connect(
            self.run_check
        )
        self.copy_button.clicked.connect(
            self.copy_report
        )
        self.close_button.clicked.connect(
            self.accept
        )

        self.check_finished.connect(
            self._on_check_finished
        )

        if auto_start:
            self.run_check()

    def run_check(self) -> None:
        if self._running:
            return

        self._running = True
        self._full_report = ""

        self.run_button.setEnabled(False)
        self.copy_button.setEnabled(False)
        self.close_button.setEnabled(False)
        self.check_completed = False

        self.status_label.setText(
            "Checking your system. "
            "The AI model test can take a little while..."
        )

        self.report_edit.setPlainText(
            "Running compatibility checks..."
        )

        self.progress.setRange(
            0,
            0,
        )

        thread = threading.Thread(
            target=self._worker,
            daemon=True,
            name="LST-SystemCheck",
        )
        thread.start()

    def _worker(self) -> None:
        try:
            results = (
                run_deep_system_check()
            )

            self.check_finished.emit(
                {
                    "ok": True,
                    "results": results,
                }
            )

        except Exception as exc:
            self.check_finished.emit(
                {
                    "ok": False,
                    "error": str(exc),
                }
            )

    def _on_check_finished(
        self,
        payload,
    ) -> None:
        self._running = False

        self.progress.setRange(
            0,
            1,
        )
        self.progress.setValue(
            1
        )

        self.run_button.setEnabled(
            True
        )
        self.close_button.setEnabled(
            True
        )
        self.check_completed = True

        if not payload.get("ok"):
            self.has_fail = True
            error = (
                payload.get("error")
                or "Unknown System Check error"
            )

            self.status_label.setText(
                "System Check could not complete."
            )

            self._full_report = (
                "LOCAL SCREEN TRANSLATOR - SYSTEM CHECK\n\n"
                "The diagnostic process itself failed.\n\n"
                f"Detected error:\n{error}\n\n"
                "How to fix:\n"
                "1. Restart Windows.\n"
                "2. Run System Check again.\n"
                "3. If the same error remains, search the web "
                "using the exact error text above.\n"
                "4. If application files are missing or blocked, "
                "reinstall the complete application."
            )

            self.report_edit.setPlainText(
                self._full_report
            )
            self.copy_button.setEnabled(
                True
            )
            return

        results = payload["results"]

        has_fail = any(
            item.status == FAIL
            for item in results
        )

        has_warn = any(
            item.status == WARN
            for item in results
        )

        self.has_fail = has_fail

        if has_fail:
            self.status_label.setText(
                "Problems were found. "
                "Follow the instructions below."
            )

        elif has_warn:
            self.status_label.setText(
                "System Check completed with warnings."
            )

        else:
            self.status_label.setText(
                "System ready - all compatibility checks passed."
            )

        self_help = format_self_help_report(
            results
        )

        technical = format_report(
            results
        )

        self._full_report = (
            self_help
            + "\n\n"
            + "=" * 60
            + "\nTECHNICAL DETAILS\n"
            + "=" * 60
            + "\n\n"
            + technical
        )

        self.report_edit.setPlainText(
            self._full_report
        )

        self.copy_button.setEnabled(
            True
        )

    def closeEvent(self, event) -> None:
        if self._running:
            event.ignore()
            return

        event.accept()

    def copy_report(self) -> None:
        if not self._full_report:
            return

        clipboard = (
            QGuiApplication.clipboard()
        )

        clipboard.setText(
            self._full_report
        )

        self.copy_button.setText(
            "Copied"
        )

        from PySide6.QtCore import QTimer

        QTimer.singleShot(
            1500,
            lambda: self.copy_button.setText(
                "Copy report"
            ),
        )
