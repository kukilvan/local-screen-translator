# Local Screen Translator

**Offline-Bildschirmübersetzer, Spieleübersetzer und OCR-Übersetzer für Windows.**  
Übersetzt Text direkt aus Spielen, Anwendungen, Browsern und Videos. OCR und Übersetzung laufen lokal auf dem PC, ohne Cloud-Übersetzungs-API.

**Version: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | Deutsch | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Funktionen

- Wort unter dem Cursor mit Kontext übersetzen;
- Absatz oder Textblock übersetzen;
- globale Hotkeys;
- HUD über Borderless Fullscreen;
- GPU-beschleunigtes PaddleOCR;
- lokale Modelle `qwen3:4b` und Riva Translate;
- integrierter System Check;
- mehrsprachige Oberfläche.

## Datenschutz

Die Übersetzung erfolgt lokal. Die mitgelieferte Ollama-Runtime nutzt `127.0.0.1:11435`.

## Installation

Alle sechs Dateien desselben Releases in einen Ordner herunterladen:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Dann `LocalScreenTranslator_Setup_1.0.0.exe` starten. Python, Ollama, PaddlePaddle, CUDA Toolkit und Modelle müssen nicht separat installiert werden.

## Anforderungen

Windows 10/11 x64, NVIDIA-GPU, Compute Capability 7.5+, 8 GB VRAM empfohlen, ca. 10 GB Speicher.

Für Spiele wird **Borderless Windowed** empfohlen.

## Download

[Windows-Installer und SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Projektlizenz: MIT. Drittanbieter-Lizenzen: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
