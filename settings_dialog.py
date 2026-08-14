from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QKeySequenceEdit,
    QLabel,
    QSpinBox,
    QVBoxLayout,
)

from autostart import (
    is_autostart_enabled,
    set_autostart,
)
from user_settings import (
    USER_SETTINGS,
    save_user_settings,
)


class SettingsDialog(QDialog):
    settings_saved = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:
        super().__init__(parent)

        self.setWindowTitle(
            "Local Screen Translator - Settings"
        )

        self.setMinimumWidth(420)

        root_layout = QVBoxLayout(
            self
        )

        form_layout = QFormLayout()

        self.language_combo = QComboBox()

        self.language_combo.addItem(
            "Russian",
            "Russian",
        )

        language_index = (
            self.language_combo.findData(
                USER_SETTINGS.target_language
            )
        )

        if language_index >= 0:
            self.language_combo.setCurrentIndex(
                language_index
            )

        form_layout.addRow(
            "Translation language:",
            self.language_combo,
        )

        self.word_hotkey_edit = QKeySequenceEdit()

        self.word_hotkey_edit.setKeySequence(
            QKeySequence(
                USER_SETTINGS.word_hotkey
            )
        )

        form_layout.addRow(
            "Word hotkey:",
            self.word_hotkey_edit,
        )

        self.paragraph_hotkey_edit = QKeySequenceEdit()

        self.paragraph_hotkey_edit.setKeySequence(
            QKeySequence(
                USER_SETTINGS.paragraph_hotkey
            )
        )

        form_layout.addRow(
            "Paragraph hotkey:",
            self.paragraph_hotkey_edit,
        )

        self.hud_timeout_spin = QSpinBox()

        self.hud_timeout_spin.setRange(
            1,
            120,
        )

        self.hud_timeout_spin.setSuffix(
            " sec"
        )

        self.hud_timeout_spin.setValue(
            max(
                1,
                USER_SETTINGS.hud_auto_hide_ms // 1000,
            )
        )

        form_layout.addRow(
            "HUD auto-hide:",
            self.hud_timeout_spin,
        )

        self.autostart_checkbox = QCheckBox(
            "Start Local Screen Translator with Windows"
        )

        self.autostart_checkbox.setChecked(
            is_autostart_enabled()
        )

        form_layout.addRow(
            "",
            self.autostart_checkbox,
        )

        root_layout.addLayout(
            form_layout
        )

        note = QLabel(
            "Currently only English → Russian translation "
            "is supported."
        )

        note.setWordWrap(
            True
        )

        root_layout.addWidget(
            note
        )

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttons.rejected.connect(
            self.reject
        )

        self.buttons.accepted.connect(
            self._save
        )

        root_layout.addWidget(
            self.buttons
        )
    def _save(self) -> None:
        word_hotkey = (
            self.word_hotkey_edit
            .keySequence()
            .toString(
                QKeySequence.SequenceFormat.PortableText
            )
        )

        paragraph_hotkey = (
            self.paragraph_hotkey_edit
            .keySequence()
            .toString(
                QKeySequence.SequenceFormat.PortableText
            )
        )

        if word_hotkey:
            USER_SETTINGS.word_hotkey = word_hotkey

        if paragraph_hotkey:
            USER_SETTINGS.paragraph_hotkey = (
                paragraph_hotkey
            )

        USER_SETTINGS.target_language = (
            self.language_combo.currentData()
        )

        USER_SETTINGS.hud_auto_hide_ms = (
            self.hud_timeout_spin.value()
            * 1000
        )

        USER_SETTINGS.autostart = (
            self.autostart_checkbox.isChecked()
        )

        set_autostart(
            USER_SETTINGS.autostart
        )

        USER_SETTINGS.first_run_completed = True

        save_user_settings(
            USER_SETTINGS
        )

        self.settings_saved.emit()

        self.accept()