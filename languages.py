from __future__ import annotations


SUPPORTED_LANGUAGES = (
    ("Russian", "ru"),
    ("Ukrainian", "uk"),
    ("German", "de"),
    ("French", "fr"),
    ("Italian", "it"),
    ("European Spanish", "es-ES"),
    ("LATAM Spanish", "es-US"),
    ("European Portuguese", "pt-PT"),
    ("Brazilian Portuguese", "pt-BR"),
    ("Polish", "pl"),
    ("Czech", "cs"),
    ("Slovak", "sk"),
    ("Danish", "da"),
    ("Finnish", "fi"),
    ("Swedish", "sv"),
    ("Norwegian", "no"),
    ("Dutch", "nl"),
    ("Greek", "el"),
    ("Hungarian", "hu"),
    ("Romanian", "ro"),
    ("Lithuanian", "lt"),
    ("Latvian", "lv"),
    ("Estonian", "et"),
    ("Slovenian", "sl"),
    ("Bulgarian", "bg"),
    ("Croatian", "hr"),
    ("Turkish", "tr"),
    ("Arabic", "ar"),
    ("Hindi", "hi"),
    ("Vietnamese", "vi"),
    ("Indonesian", "id"),
    ("Thai", "th"),
    ("Simplified Chinese", "zh-CN"),
    ("Traditional Chinese", "zh-TW"),
    ("Japanese", "ja"),
    ("Korean", "ko"),
)


LANGUAGE_CODES = {
    name: code
    for name, code in SUPPORTED_LANGUAGES
}


def get_language_code(
    language_name: str,
) -> str:
    try:
        return LANGUAGE_CODES[
            language_name
        ]

    except KeyError as exc:
        raise ValueError(
            f"Unsupported language: {language_name}"
        ) from exc