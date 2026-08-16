# Local Screen Translator

**Traducteur d'écran hors ligne, traducteur de jeux et traducteur OCR pour Windows.**  
Traduit directement le texte des jeux, applications, navigateurs et vidéos. L'OCR et la traduction sont exécutés localement, sans API cloud de traduction.

**Version : 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | Français | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | [한국어](README_KO.md)

## Fonctions

- traduction du mot sous le curseur avec contexte ;
- traduction d'un paragraphe ;
- raccourcis globaux ;
- HUD au-dessus du Borderless Fullscreen ;
- PaddleOCR accéléré par GPU ;
- modèles locaux `qwen3:4b` et Riva Translate ;
- System Check intégré ;
- interface multilingue.

## Confidentialité

La traduction est locale. Ollama inclus fonctionne sur `127.0.0.1:11435`.

## Installation

Téléchargez les six fichiers du même release dans un seul dossier :

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

Lancez `LocalScreenTranslator_Setup_1.0.0.exe`. Aucun besoin d'installer séparément Python, Ollama, PaddlePaddle, CUDA Toolkit ou les modèles.

## Configuration requise

Windows 10/11 x64, GPU NVIDIA, Compute Capability 7.5+, 8 Go de VRAM recommandés et environ 10 Go d'espace.

Pour les jeux, **Borderless Windowed** offre généralement la meilleure compatibilité.

## Télécharger

[Installateur Windows et SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

Licence du projet : MIT. Licences tierces : `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
