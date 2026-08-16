from __future__ import annotations

from ui_i18n import (
    detect_system_language,
    resolve_ui_language,
)


SC_TRANSLATIONS = {
    "en": {
        "system_check": "System Check",
        "description": (
            "Checks GPU, OCR, screen capture, local AI models, "
            "alignment and Windows speech."
        ),
        "ready_to_check": "Ready to check.",
        "checking": (
            "Checking system compatibility. "
            "The AI model test can take a little while..."
        ),
        "placeholder": "System Check results will appear here.",
        "run_again": "Run again",
        "copy_report": "Copy report",
        "close": "Close",
        "copied": "Copied",
        "status_ready": (
            "System ready - all compatibility checks passed."
        ),
        "status_warnings": (
            "System Check completed with warnings."
        ),
        "status_problems": (
            "Problems were found. Follow the instructions below."
        ),
        "status_failed": (
            "System Check could not complete."
        ),
        "technical_details": "TECHNICAL DETAILS",
    },

    "ru": {
        "system_check": "Проверка системы",
        "description": (
            "Проверяет GPU, OCR, захват экрана, локальные ИИ-модели, "
            "выравнивание текста и синтез речи Windows."
        ),
        "ready_to_check": "Готово к проверке.",
        "checking": (
            "Проверка совместимости системы. "
            "Тест ИИ-моделей может занять некоторое время..."
        ),
        "placeholder": "Здесь появятся результаты проверки системы.",
        "run_again": "Проверить снова",
        "copy_report": "Копировать отчёт",
        "close": "Закрыть",
        "copied": "Скопировано",
        "status_ready": (
            "Система готова — все проверки совместимости пройдены."
        ),
        "status_warnings": (
            "Проверка системы завершена с предупреждениями."
        ),
        "status_problems": (
            "Обнаружены проблемы. Следуйте инструкциям ниже."
        ),
        "status_failed": (
            "Не удалось завершить проверку системы."
        ),
        "technical_details": "ТЕХНИЧЕСКИЕ ДАННЫЕ",
    },
}


def current_system_check_language() -> str:
    try:
        from user_settings import USER_SETTINGS

        return resolve_ui_language(
            USER_SETTINGS.ui_language
        )

    except Exception:
        return detect_system_language()


def sc_t(
    key: str,
    language: str | None = None,
) -> str:
    language = (
        language
        or current_system_check_language()
    )

    table = SC_TRANSLATIONS.get(
        language,
        SC_TRANSLATIONS["en"],
    )

    return table.get(
        key,
        SC_TRANSLATIONS["en"].get(
            key,
            key,
        ),
    )
