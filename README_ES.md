# Local Screen Translator

**Traductor de pantalla sin conexión, traductor para juegos y traductor OCR para Windows.**  
Traduce texto directamente desde juegos, aplicaciones, navegadores y vídeo. El OCR y la traducción se ejecutan localmente sin una API de traducción en la nube.

**Versión: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | Español | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Funciones

- traducción de la palabra bajo el cursor con contexto;
- traducción de párrafos;
- atajos globales;
- HUD sobre Borderless Fullscreen;
- PaddleOCR acelerado por GPU;
- modelos locales `qwen3:4b` y Riva Translate;
- System Check integrado;
- interfaz multilingüe.

## Privacidad

La traducción es local. Ollama incluido usa `127.0.0.1:11435`.

## Instalación

Descarga los seis archivos del mismo release en una sola carpeta:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Ejecuta `LocalScreenTranslator_Setup_1.0.0.exe`. No hace falta instalar por separado Python, Ollama, PaddlePaddle, CUDA Toolkit ni los modelos.

## Requisitos

Windows 10/11 x64, GPU NVIDIA, Compute Capability 7.5+, 8 GB de VRAM recomendados y unos 10 GB de espacio.

Para juegos se recomienda **Borderless Windowed**.

## Descargar

[Instalador de Windows y SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Licencia del proyecto: MIT. Licencias de terceros: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
