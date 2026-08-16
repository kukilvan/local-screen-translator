# Local Screen Translator

**Tradutor de tela offline, tradutor para jogos e tradutor OCR para Windows.**  
Traduz texto diretamente de jogos, aplicativos, navegadores e vídeos. OCR e tradução são executados localmente, sem API de tradução em nuvem.

**Versão: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | Português (Brasil) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Recursos

- tradução da palavra sob o cursor com contexto;
- tradução de parágrafos;
- atalhos globais;
- HUD sobre Borderless Fullscreen;
- PaddleOCR acelerado por GPU;
- modelos locais `qwen3:4b` e Riva Translate;
- System Check integrado;
- interface multilíngue.

## Privacidade

A tradução é local. O Ollama incluído usa `127.0.0.1:11435`.

## Instalação

Baixe os seis arquivos do mesmo release para uma única pasta:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Execute `LocalScreenTranslator_Setup_1.0.0.exe`. Não é necessário instalar Python, Ollama, PaddlePaddle, CUDA Toolkit ou os modelos separadamente.

## Requisitos

Windows 10/11 x64, GPU NVIDIA, Compute Capability 7.5+, 8 GB de VRAM recomendados e cerca de 10 GB de espaço.

Para jogos, use preferencialmente **Borderless Windowed**.

## Download

[Instalador Windows e SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Licença do projeto: MIT. Licenças de terceiros: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
