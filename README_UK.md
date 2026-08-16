# Local Screen Translator

**Локальний екранний перекладач, перекладач ігор та OCR-перекладач для Windows.**  
Перекладає текст безпосередньо з ігор, програм, браузерів і відео. OCR та переклад працюють локально на ПК без хмарного API.

**Версія: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | Українська | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Можливості

- переклад слова під курсором з контекстом;
- переклад абзацу або блоку тексту;
- глобальні гарячі клавіші;
- HUD поверх Borderless Fullscreen;
- GPU-прискорений PaddleOCR;
- локальні `qwen3:4b` і Riva Translate;
- System Check та діагностичні коди;
- багатомовний інтерфейс.

## Приватність

Переклад локальний. Вбудований Ollama працює на `127.0.0.1:11435`.

## Встановлення

Завантажте всі шість файлів одного релізу в одну папку:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Запустіть `LocalScreenTranslator_Setup_1.0.0.exe`. Окремо Python, Ollama, PaddlePaddle, CUDA Toolkit та моделі встановлювати не потрібно.

## Вимоги

Windows 10/11 x64, NVIDIA GPU, Compute Capability 7.5+, рекомендовано 8 ГБ VRAM та приблизно 10 ГБ місця.

Для ігор найкраще підходить **Borderless Windowed**.

## Завантажити

[Windows installer та SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Проєкт: MIT. Ліцензії сторонніх компонентів: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
