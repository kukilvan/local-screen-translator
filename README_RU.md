# Local Screen Translator

**Локальный экранный переводчик, переводчик игр и OCR-переводчик для Windows.**  
Переводит текст прямо с экрана в играх, программах, браузерах и видео. OCR и перевод работают локально на ПК без облачного API перевода.

**Версия: 1.0.0**

[English](README.md) | Русский | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Возможности

- перевод слова под курсором с учетом контекста;
- перевод абзаца или блока текста;
- настраиваемые глобальные горячие клавиши;
- HUD поверх обычных окон и Borderless Fullscreen;
- GPU-ускоренный PaddleOCR;
- локальные модели `qwen3:4b` и Riva Translate;
- встроенный System Check и диагностические коды;
- многоязычный интерфейс;
- произношение английских слов голосами Windows.

## Конфиденциальность

Перевод выполняется локально. Встроенный Ollama работает на `127.0.0.1:11435`. Захваченный текст не предназначен для отправки во внешние сервисы перевода.

## Установка

Скачайте **все шесть файлов** одного релиза и положите их в одну папку:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Запустите `LocalScreenTranslator_Setup_1.0.0.exe`. `.bin` — обязательные части установщика.

Python, Ollama, PaddlePaddle, CUDA Toolkit, OCR-модели и модели перевода отдельно устанавливать не нужно.

## Требования

Windows 10/11 x64, NVIDIA GPU, Compute Capability 7.5+, рекомендуется 8 ГБ VRAM и около 10 ГБ места.

Для лучшей совместимости с играми используйте **Borderless Windowed**.

## Безопасность

v1.0.0 пока не имеет цифровой подписи. Smart App Control или репутационная защита Windows могут блокировать неподписанный EXE. Не отключайте защиту Windows только ради запуска программы.

## Скачать

[Windows installer и SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Лицензия проекта — MIT. Лицензии сторонних компонентов: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
