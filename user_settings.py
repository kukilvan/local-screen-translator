import json
import os
from dataclasses import asdict, dataclass


APP_DIR = os.path.join(
    os.environ.get("APPDATA", os.path.expanduser("~")),
    "LocalScreenTranslator",
)

SETTINGS_PATH = os.path.join(
    APP_DIR,
    "settings.json",
)


@dataclass
class UserSettings:
    ui_language: str = "auto"
    target_language: str = "Russian"
    tts_voice_id: str = ""

    word_hotkey: str = "Ctrl+Alt+Space"
    paragraph_hotkey: str = "Ctrl+Alt+Shift+Space"

    hud_auto_hide_ms: int = 12000

    autostart: bool = False

    first_run_completed: bool = False


def load_user_settings() -> UserSettings:
    if not os.path.exists(SETTINGS_PATH):
        return UserSettings()

    try:
        with open(
            SETTINGS_PATH,
            "r",
            encoding="utf-8",
        ) as file:
            raw = json.load(file)

        defaults = UserSettings()

        return UserSettings(
            ui_language=raw.get(
                "ui_language",
                defaults.ui_language,
            ),
            target_language=raw.get(
                "target_language",
                defaults.target_language,
            ),
            tts_voice_id=raw.get(
                "tts_voice_id",
                defaults.tts_voice_id,
            ),
            word_hotkey=raw.get(
                "word_hotkey",
                defaults.word_hotkey,
            ),
            paragraph_hotkey=raw.get(
                "paragraph_hotkey",
                defaults.paragraph_hotkey,
            ),
            hud_auto_hide_ms=raw.get(
                "hud_auto_hide_ms",
                defaults.hud_auto_hide_ms,
            ),
            autostart=raw.get(
                "autostart",
                defaults.autostart,
            ),
            first_run_completed=raw.get(
                "first_run_completed",
                defaults.first_run_completed,
            ),
        )

    except (
        OSError,
        json.JSONDecodeError,
        TypeError,
        ValueError,
    ):
        return UserSettings()


def save_user_settings(
    settings: UserSettings,
) -> None:
    os.makedirs(
        APP_DIR,
        exist_ok=True,
    )

    temp_path = SETTINGS_PATH + ".tmp"

    with open(
        temp_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            asdict(settings),
            file,
            ensure_ascii=False,
            indent=2,
        )

    os.replace(
        temp_path,
        SETTINGS_PATH,
    )


USER_SETTINGS = load_user_settings()
