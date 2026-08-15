from __future__ import annotations

import json
import re
import subprocess
import tempfile
import uuid
from pathlib import Path


ENGLISH_VOICE_PACKS = (
    ("en-US", "English (United States)"),
    ("en-GB", "English (United Kingdom)"),
    ("en-AU", "English (Australia)"),
    ("en-CA", "English (Canada)"),
    ("en-IE", "English (Ireland)"),
    ("en-IN", "English (India)"),
)


_LOCALE_RE = re.compile(
    r"^[a-z]{2}-[A-Z]{2}$"
)

_SHARED_DIR = Path(
    r"C:\ProgramData\LocalScreenTranslator"
)


def capability_name(
    locale: str,
) -> str:
    if not _LOCALE_RE.fullmatch(locale):
        raise ValueError(
            f"Invalid locale: {locale!r}"
        )

    return (
        "Language.TextToSpeech~~~"
        f"{locale}"
        "~0.0.1.0"
    )


def install_voice_pack(
    locale: str,
) -> dict:
    """
    Install a Microsoft Windows TTS language capability.

    The servicing process runs elevated and hidden.
    Windows may show the normal UAC confirmation.
    """
    capability = capability_name(locale)

    result_path = (
        _SHARED_DIR
        / f"voice_install_result_{uuid.uuid4().hex}.json"
    )

    with tempfile.TemporaryDirectory(
        prefix="lst_voice_"
    ) as temp_dir:
        temp_dir = Path(temp_dir)

        elevated_script = (
            temp_dir
            / "install_voice.ps1"
        )

        capability_ps = capability.replace(
            "'",
            "''",
        )

        result_ps = str(
            result_path
        ).replace(
            "'",
            "''",
        )

        elevated_script.write_text(
            f'''
$ErrorActionPreference = "Stop"

$sharedDir = "C:\\ProgramData\\LocalScreenTranslator"
$resultPath = '{result_ps}'
$capabilityName = '{capability_ps}'

New-Item `
    -ItemType Directory `
    -Path $sharedDir `
    -Force | Out-Null

try {{
    $before = Get-WindowsCapability `
        -Online `
        -Name $capabilityName `
        -ErrorAction Stop

    if ($null -eq $before) {{
        throw "Capability was not found."
    }}

    $initialState = [string]$before.State
    $restartNeeded = $false

    if ($initialState -ne "Installed") {{
        $installResult = Add-WindowsCapability `
            -Online `
            -Name $capabilityName `
            -ErrorAction Stop

        $restartNeeded = [bool]$installResult.RestartNeeded
    }}

    $after = Get-WindowsCapability `
        -Online `
        -Name $capabilityName `
        -ErrorAction Stop

    $finalState = [string]$after.State
    $ok = ($finalState -eq "Installed")

    [ordered]@{{
        ok = $ok
        capability = $capabilityName
        initial_state = $initialState
        final_state = $finalState
        restart_needed = $restartNeeded
        error = ""
    }} |
        ConvertTo-Json -Compress |
        Set-Content `
            -LiteralPath $resultPath `
            -Encoding UTF8
}}
catch {{
    [ordered]@{{
        ok = $false
        capability = $capabilityName
        initial_state = ""
        final_state = ""
        restart_needed = $false
        error = $_.Exception.Message
    }} |
        ConvertTo-Json -Compress |
        Set-Content `
            -LiteralPath $resultPath `
            -Encoding UTF8
}}
''',
            encoding="utf-8",
        )

        wrapper_script = (
            temp_dir
            / "launch_elevated.ps1"
        )

        elevated_path_ps = str(
            elevated_script
        ).replace(
            "'",
            "''",
        )

        wrapper_script.write_text(
            f'''
$ErrorActionPreference = "Stop"

try {{
    $process = Start-Process powershell.exe `
        -Verb RunAs `
        -WindowStyle Hidden `
        -Wait `
        -PassThru `
        -ArgumentList @(
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-WindowStyle", "Hidden",
            "-File", '"{elevated_path_ps}"'
        )

    exit $process.ExitCode
}}
catch {{
    exit 1223
}}
''',
            encoding="utf-8",
        )

        flags = getattr(
            subprocess,
            "CREATE_NO_WINDOW",
            0,
        )

        try:
            process = subprocess.run(
                [
                    "powershell.exe",
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-WindowStyle",
                    "Hidden",
                    "-File",
                    str(wrapper_script),
                ],
                capture_output=True,
                text=True,
                creationflags=flags,
                timeout=900,
            )

        except subprocess.TimeoutExpired:
            return {
                "ok": False,
                "capability": capability,
                "initial_state": "",
                "final_state": "",
                "restart_needed": False,
                "error": "Installation timed out.",
            }

        if result_path.exists():
            try:
                result = json.loads(
                    result_path.read_text(
                        encoding="utf-8-sig"
                    )
                )

                return result

            except Exception as exc:
                return {
                    "ok": False,
                    "capability": capability,
                    "initial_state": "",
                    "final_state": "",
                    "restart_needed": False,
                    "error": (
                        "Could not read installation result: "
                        f"{exc}"
                    ),
                }

        if process.returncode == 1223:
            error = "UAC was cancelled."
        else:
            error = (
                process.stderr.strip()
                or process.stdout.strip()
                or "Elevated installation did not return a result."
            )

        return {
            "ok": False,
            "capability": capability,
            "initial_state": "",
            "final_state": "",
            "restart_needed": False,
            "error": error,
        }
