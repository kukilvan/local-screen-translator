# Local Screen Translator

**Offline'owy tłumacz ekranu, tłumacz gier i tłumacz OCR dla Windows.**  
Tłumaczy tekst bezpośrednio z gier, aplikacji, przeglądarek i wideo. OCR i tłumaczenie działają lokalnie bez chmurowego API.

**Wersja: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | Polski | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Funkcje

- tłumaczenie słowa pod kursorem z kontekstem;
- tłumaczenie akapitów;
- globalne skróty klawiszowe;
- HUD nad Borderless Fullscreen;
- PaddleOCR z akceleracją GPU;
- lokalne modele `qwen3:4b` i Riva Translate;
- wbudowany System Check;
- wielojęzyczny interfejs.

## Prywatność

Tłumaczenie jest lokalne. Dołączony Ollama działa na `127.0.0.1:11435`.

## Instalacja

Pobierz sześć plików tego samego wydania do jednego folderu:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Uruchom `LocalScreenTranslator_Setup_1.0.0.exe`. Python, Ollama, PaddlePaddle, CUDA Toolkit i modele nie wymagają osobnej instalacji.

## Wymagania

Windows 10/11 x64, GPU NVIDIA, Compute Capability 7.5+, zalecane 8 GB VRAM i około 10 GB miejsca.

Do gier zalecany jest **Borderless Windowed**.

## Pobieranie

[Instalator Windows i SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Licencja projektu: MIT. Licencje zewnętrzne: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
