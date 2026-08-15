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
from languages import SUPPORTED_LANGUAGES
from ui_i18n import UI_LANGUAGES, t
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
            t("settings_title")
        )

        self.setMinimumWidth(420)

        root_layout = QVBoxLayout(
            self
        )

        form_layout = QFormLayout()

        self.ui_language_combo = QComboBox()

        for language_code, language_name in UI_LANGUAGES:
            self.ui_language_combo.addItem(
                language_name,
                language_code,
            )

        ui_language_index = self.ui_language_combo.findData(
            USER_SETTINGS.ui_language
        )

        if ui_language_index >= 0:
            self.ui_language_combo.setCurrentIndex(
                ui_language_index
            )

        form_layout.addRow(
            t("interface_language"),
            self.ui_language_combo,
        )

        self.language_combo = QComboBox()

        for (
            language_name,
            language_code,
        ) in SUPPORTED_LANGUAGES:
            self.language_combo.addItem(
                language_name,
                language_name,
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
            t("translation_language"),
            self.language_combo,
        )

        self.word_hotkey_edit = QKeySequenceEdit()

        self.word_hotkey_edit.setKeySequence(
            QKeySequence(
                USER_SETTINGS.word_hotkey
            )
        )

        form_layout.addRow(
            t("word_hotkey"),
            self.word_hotkey_edit,
        )

        self.paragraph_hotkey_edit = QKeySequenceEdit()

        self.paragraph_hotkey_edit.setKeySequence(
            QKeySequence(
                USER_SETTINGS.paragraph_hotkey
            )
        )

        form_layout.addRow(
            t("paragraph_hotkey"),
            self.paragraph_hotkey_edit,
        )

        self.hud_timeout_spin = QSpinBox()

        self.hud_timeout_spin.setRange(
            1,
            120,
        )

        self.hud_timeout_spin.setSuffix(
            t("seconds")
        )

        self.hud_timeout_spin.setValue(
            max(
                1,
                USER_SETTINGS.hud_auto_hide_ms // 1000,
            )
        )

        form_layout.addRow(
            t("hud_auto_hide"),
            self.hud_timeout_spin,
        )

        self.autostart_checkbox = QCheckBox(
            t("autostart")
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
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        
        save_button = self.buttons.button(
            QDialogButtonBox.StandardButton.Save
        )
        cancel_button = self.buttons.button(
            QDialogButtonBox.StandardButton.Cancel
        )

        if save_button is not None:
            save_button.setText(
                t("save")
            )

        if cancel_button is not None:
            cancel_button.setText(
                t("cancel")
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

        USER_SETTINGS.ui_language = (
            self.ui_language_combo.currentData()
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



