# Local Screen Translator

**Offline screen translator, game translator and OCR translator for Windows.**
Local Screen Translator translates text directly from games, applications, browsers and video while keeping OCR and translation processing on your PC.

Version: **1.0.0**

**Languages:** English | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português (Brasil)](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)


## Main features

- Translate the word under the mouse cursor with surrounding context.
- Translate a paragraph or nearby block of text.
- Global configurable hotkeys.
- Popup HUD displayed over normal and borderless fullscreen applications.
- English word pronunciation using Microsoft Windows voices.
- GPU accelerated OCR.
- Local translation models.
- Built-in System Check with self-service diagnostic error codes.
- Multilingual application interface.
- No external cloud translation API.

Default hotkeys:

- `Ctrl + Alt + Space` - translate the word under the cursor.
- `Ctrl + Alt + Shift + Space` - translate the nearby paragraph.

## Privacy

Translation is performed locally.

The application uses its own bundled Ollama runtime on:

`127.0.0.1:11435`

The translation client is restricted to loopback/local communication.

Captured text is not intentionally sent to an external translation service.

## Installation

Download **all six installer files** from the same release:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Keep all six files in the same folder and run:

`LocalScreenTranslator_Setup_1.0.0.exe`

The `.bin` files are required parts of the installer and should not be opened
individually.

You do **not** need to manually install:

- Python
- Ollama
- PaddlePaddle
- CUDA Toolkit
- translation models
- OCR models

They are included with the application where required.

## System requirements

Current version:

- Windows 10 or Windows 11 64-bit
- NVIDIA GPU
- NVIDIA driver compatible with the bundled CUDA/Paddle runtime
- Compute Capability 7.5 or newer
- 8 GB VRAM recommended
- Approximately 10 GB of free disk space for the installed application

The built-in System Check verifies the actual machine before normal use.

## How it works

### Screen capture

Screen capture is performed through DXcam / Windows Desktop Duplication.

Capture is requested when translation is triggered rather than continuously
recording the screen in the background.

### OCR

Text recognition uses PaddleOCR with bundled OCR models and GPU acceleration.

Current OCR assets include:

- PP-OCRv6 small detection model
- Latin PP-OCRv5 mobile recognition model

### Word translation

Word mode uses the local `qwen3:4b` model together with surrounding OCR
context to determine the appropriate translation of the word under the cursor.

### Paragraph translation

Paragraph mode uses the bundled Riva Translate model.

The current packaged model is based on:

`nvidia/Riva-Translate-4B-Instruct-v2`

and is distributed in quantized GGUF form.

### Word alignment

SimAlign and multilingual BERT are used for source/target alignment where
required by the translation pipeline.

### Speech

English pronunciation uses Microsoft Windows speech capabilities. Available
voices depend on the Windows voice packages installed on the computer.

## System Check

Local Screen Translator includes a compatibility and runtime diagnostic system.

It checks, among other things:

- Windows architecture
- NVIDIA GPU
- NVIDIA driver
- GPU compute capability
- available VRAM
- screen capture
- PaddleOCR GPU runtime
- bundled application assets
- local Ollama runtime
- required translation models
- alignment worker
- Microsoft speech
- writable application data directory
- local port 11435

When a failure is detected the application provides a stable diagnostic code
such as `LST-GPU-001`, `LST-AI-001` or `LST-CAP-001` together with suggested
self-service actions.

## Multiple NVIDIA GPUs

Version 1.0.0 currently uses NVIDIA GPU 0 for its GPU processing pipeline.

If more than one NVIDIA GPU is installed, System Check shows which GPU is
being used.

## Fullscreen applications

Borderless Windowed mode generally provides the best compatibility.

Some games, exclusive fullscreen modes, anti-cheat systems or protected
content may prevent screen capture or overlay display.

## Windows security and code signing

Version 1.0.0 release binaries are currently not digitally code-signed.

Depending on Windows security configuration, reputation-based protection or
Smart App Control may block an unsigned executable.

Do not disable or weaken Windows security features solely to run the
application.

## Troubleshooting

Start with the built-in **System Check**.

If an error appears:

1. Note the complete `LST-...` error code.
2. Read the self-help instructions shown by the application.
3. Check Windows Security protection history if an application file appears
   to be missing.
4. Reinstall using the complete installer set if files were removed.

Do not manually download random DLL files or replacement model files from
untrusted websites.

## Building from source

The repository contains the Python application source and development
requirements.

The public installer is a standalone distribution. End users do not need the
development environment.

Main development dependency files:

- `requirements.txt`
- `requirements-paddle.txt`
- `requirements-align.txt`

The release build uses separate main and alignment-worker environments.

## Third-party software and models

This project includes or redistributes third-party software and model weights
under their respective licenses.

See:

- `THIRD_PARTY_NOTICES.md`
- `NOTICE`
- `third_party_licenses/`

The MIT license of Local Screen Translator itself does **not** replace or
override licenses that apply to bundled third-party components or models.

## License

Local Screen Translator source code is released under the MIT License.

See `LICENSE`.

## Releases

Release packages and checksums are published in the repository Releases
section:

https://github.com/kukilvan/local-screen-translator/releases
