from __future__ import annotations

import asyncio
import threading


PREFERRED_DEFAULT_VOICE = "Microsoft Mark"


def get_installed_english_voices() -> list[dict[str, str]]:
    """
    Return installed English Windows voices visible through
    Windows.Media.SpeechSynthesis.
    """
    try:
        from winrt.windows.media.speechsynthesis import (
            SpeechSynthesizer,
        )

        result = []

        for voice in SpeechSynthesizer.all_voices:
            language = str(
                voice.language or ""
            )

            if not language.lower().startswith("en"):
                continue

            result.append(
                {
                    "id": str(voice.id),
                    "name": str(voice.display_name),
                    "language": language,
                    "gender": (
                        "Male"
                        if int(voice.gender) == 0
                        else "Female"
                    ),
                }
            )

        return result

    except Exception:
        return []


def _select_voice(
    synthesizer,
    requested_voice_id: str | None,
):
    from winrt.windows.media.speechsynthesis import (
        SpeechSynthesizer,
    )

    voices = [
        voice
        for voice in SpeechSynthesizer.all_voices
        if str(
            voice.language or ""
        ).lower().startswith("en")
    ]

    if not voices:
        return None

    if requested_voice_id:
        for voice in voices:
            if str(voice.id) == requested_voice_id:
                return voice

    for voice in voices:
        if (
            str(voice.display_name)
            == PREFERRED_DEFAULT_VOICE
        ):
            return voice

    return voices[0]


async def _speak_winrt_async(
    text: str,
    voice_id: str | None = None,
) -> None:
    from winrt.windows.media.playback import (
        MediaPlayer,
        MediaPlayerAudioCategory,
    )
    from winrt.windows.media.speechsynthesis import (
        SpeechSynthesizer,
    )

    synthesizer = SpeechSynthesizer()

    selected_voice = _select_voice(
        synthesizer,
        voice_id,
    )

    if selected_voice is not None:
        synthesizer.voice = selected_voice

    stream = await (
        synthesizer.synthesize_text_to_stream_async(
            text
        )
    )

    player = MediaPlayer()
    player.audio_category = (
        MediaPlayerAudioCategory.SPEECH
    )
    player.set_stream_source(stream)

    finished = asyncio.Event()
    loop = asyncio.get_running_loop()

    def on_ended(sender, args):
        loop.call_soon_threadsafe(
            finished.set
        )

    token = player.add_media_ended(
        on_ended
    )

    try:
        player.play()

        await asyncio.wait_for(
            finished.wait(),
            timeout=20,
        )

    finally:
        try:
            player.remove_media_ended(
                token
            )
        except Exception:
            pass

        try:
            player.close()
        except Exception:
            pass


def _speak_sapi_sync(
    text: str,
) -> None:
    """
    Fallback for systems where WinRT speech is unavailable.
    """
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

            if "Mark" in description:
                selected = token
                break

            if "Zira" in description:
                selected = token

        if selected is not None:
            voice.Voice = selected

        voice.Rate = 0
        voice.Volume = 100
        voice.Speak(text)

    finally:
        comtypes.CoUninitialize()


def _speak_sync(
    text: str,
    voice_id: str | None = None,
) -> None:
    text = (
        text
        or ""
    ).strip()

    if not text:
        return

    try:
        asyncio.run(
            _speak_winrt_async(
                text,
                voice_id,
            )
        )

    except Exception as exc:
        print(
            "WINRT TTS FALLBACK:",
            repr(exc),
            flush=True,
        )

        _speak_sapi_sync(
            text
        )


def speak_english(
    text: str,
    voice_id: str | None = None,
) -> None:
    thread = threading.Thread(
        target=_speak_sync,
        args=(
            text,
            voice_id,
        ),
        daemon=True,
        name="LST-Speech",
    )

    thread.start()


def test_speech(
    text: str = "translation",
    voice_id: str | None = None,
) -> None:
    _speak_sync(
        text,
        voice_id,
    )
