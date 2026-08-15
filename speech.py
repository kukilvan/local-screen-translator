from __future__ import annotations

import threading


def _speak_sync(
    text: str,
) -> None:
    text = (text or "").strip()

    if not text:
        return

    import comtypes
    from comtypes.client import CreateObject

    comtypes.CoInitialize()

    try:
        voice = CreateObject(
            "SAPI.SpVoice",
            dynamic=True,
        )

        voices = voice.GetVoices(
            "Language=409"
        )

        selected = None

        for index in range(
            voices.Count
        ):
            token = voices.Item(index)

            description = (
                token.GetDescription()
                or ""
            )

            if selected is None:
                selected = token

            if "Zira" in description:
                selected = token
                break

        if selected is not None:
            voice.Voice = selected

        voice.Rate = 0
        voice.Volume = 100

        voice.Speak(text)

    finally:
        comtypes.CoUninitialize()


def speak_english(
    text: str,
) -> None:
    thread = threading.Thread(
        target=_speak_sync,
        args=(text,),
        daemon=True,
        name="LST-Speech",
    )

    thread.start()


def test_speech(
    text: str = "translation",
) -> None:
    _speak_sync(text)
