from __future__ import annotations

import sys
import winreg
from pathlib import Path


APP_NAME = "LocalScreenTranslator"

RUN_KEY_PATH = (
    r"Software\Microsoft\Windows"
    r"\CurrentVersion\Run"
)


def _autostart_command() -> str:
    if getattr(
        sys,
        "frozen",
        False,
    ):
        return f'"{sys.executable}"'

    project_dir = Path(
        __file__
    ).resolve().parent

    pythonw_path = (
        project_dir
        / ".venv"
        / "Scripts"
        / "pythonw.exe"
    )

    app_path = (
        project_dir
        / "app.py"
    )

    return (
        f'"{pythonw_path}" '
        f'"{app_path}"'
    )


def set_autostart(
    enabled: bool,
) -> None:
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        RUN_KEY_PATH,
        0,
        winreg.KEY_SET_VALUE,
    ) as key:
        if enabled:
            winreg.SetValueEx(
                key,
                APP_NAME,
                0,
                winreg.REG_SZ,
                _autostart_command(),
            )

        else:
            try:
                winreg.DeleteValue(
                    key,
                    APP_NAME,
                )
            except FileNotFoundError:
                pass


def is_autostart_enabled() -> bool:
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            RUN_KEY_PATH,
            0,
            winreg.KEY_QUERY_VALUE,
        ) as key:
            winreg.QueryValueEx(
                key,
                APP_NAME,
            )

        return True

    except FileNotFoundError:
        return False