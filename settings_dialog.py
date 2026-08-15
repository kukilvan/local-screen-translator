from __future__ import annotations

import threading

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
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)

from autostart import (
    is_autostart_enabled,
    set_autostart,
)
from languages import SUPPORTED_LANGUAGES
from speech import get_installed_english_voices
from ui_i18n import UI_LANGUAGES, t
from voice_packs import (
    ENGLISH_VOICE_PACKS,
    install_voice_pack,
)
from user_settings import (
    USER_SETTINGS,
    save_user_settings,
)


class SettingsDialog(QDialog):
    settings_saved = Signal()
    voice_install_finished = Signal(object)

    def __init__(
        self,
        parent=None,
    ) -> None:
        super().__init__(parent)

        self.voice_install_finished.connect(
            self._on_voice_install_finished
        )

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

        self.voice_combo = QComboBox()
        self._refresh_voice_combo()

        form_layout.addRow(
            t("pronunciation_voice"),
            self.voice_combo,
        )

        self.voice_pack_combo = QComboBox()

        for locale, _display_name in ENGLISH_VOICE_PACKS:
            self.voice_pack_combo.addItem(
                locale,
                locale,
            )

        form_layout.addRow(
            t("microsoft_voice_pack"),
            self.voice_pack_combo,
        )

        self.install_voice_button = QPushButton(
            t("install_voice_pack")
        )

        self.install_voice_button.clicked.connect(
            self._install_selected_voice_pack
        )

        form_layout.addRow(
            "",
            self.install_voice_button,
        )

        self.voice_install_status = QLabel("")
        self.voice_install_status.setWordWrap(True)

        form_layout.addRow(
            "",
            self.voice_install_status,
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
    def _refresh_voice_combo(self) -> None:
        if not hasattr(
            self,
            "voice_combo",
        ):
            return

        selected_id = (
            self.voice_combo.currentData()
            if self.voice_combo.count()
            else USER_SETTINGS.tts_voice_id
        )

        selected_id = (
            selected_id
            or USER_SETTINGS.tts_voice_id
            or ""
        )

        self.voice_combo.clear()

        self.voice_combo.addItem(
            t("automatic_voice"),
            "",
        )

        for voice in get_installed_english_voices():
            label = (
                f"{voice['name']} ? "
                f"{voice['language']} ? "
                f"{voice['gender']}"
            )

            self.voice_combo.addItem(
                label,
                voice["id"],
            )

        index = self.voice_combo.findData(
            selected_id
        )

        if index < 0:
            index = 0

        self.voice_combo.setCurrentIndex(
            index
        )

    def _install_selected_voice_pack(self) -> None:
        locale = self.voice_pack_combo.currentData()

        if not locale:
            return

        self.install_voice_button.setEnabled(
            False
        )
        self.voice_pack_combo.setEnabled(
            False
        )

        self.install_voice_button.setText(
            t("installing_voice_pack")
        )

        self.voice_install_status.setText(
            t("installing_voice_pack_status").format(
                locale=locale
            )
        )

        thread = threading.Thread(
            target=self._voice_install_worker,
            args=(locale,),
            daemon=True,
            name="LST-VoicePackInstaller",
        )

        thread.start()

    def _voice_install_worker(
        self,
        locale: str,
    ) -> None:
        try:
            result = install_voice_pack(
                locale
            )

        except Exception as exc:
            result = {
                "ok": False,
                "restart_needed": False,
                "error": str(exc),
            }

        result["locale"] = locale

        self.voice_install_finished.emit(
            result
        )

    def _on_voice_install_finished(
        self,
        result,
    ) -> None:
        self.install_voice_button.setEnabled(
            True
        )
        self.voice_pack_combo.setEnabled(
            True
        )

        self.install_voice_button.setText(
            t("install_voice_pack")
        )

        locale = result.get(
            "locale",
            "",
        )

        if result.get("ok"):
            self._refresh_voice_combo()

            if result.get(
                "restart_needed"
            ):
                message = t(
                    "voice_pack_restart"
                ).format(
                    locale=locale
                )

            else:
                message = t(
                    "voice_pack_installed"
                ).format(
                    locale=locale
                )

            self.voice_install_status.setText(
                message
            )

        else:
            error = (
                result.get("error")
                or "Unknown error"
            )

            self.voice_install_status.setText(
                t(
                    "voice_pack_install_error"
                ).format(
                    error=error
                )
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

        USER_SETTINGS.tts_voice_id = (
            self.voice_combo.currentData()
            or ""
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



