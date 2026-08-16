# Local Screen Translator

**Windows 向けオフライン画面翻訳・ゲーム翻訳・OCR 翻訳ツール。**  
ゲーム、アプリ、ブラウザー、動画の文字を直接翻訳します。OCR と翻訳は PC 上でローカル実行され、クラウド翻訳 API を使用しません。

**バージョン: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | 日本語 | [한국어](README_KO.md)

## 主な機能

- カーソル下の単語を文脈付きで翻訳；
- 段落翻訳；
- グローバルホットキー；
- Borderless Fullscreen 上の HUD；
- GPU 対応 PaddleOCR；
- ローカル `qwen3:4b` と Riva Translate；
- System Check；
- 多言語 UI。

## プライバシー

翻訳はローカルです。付属 Ollama は `127.0.0.1:11435` を使用します。

## インストール

同じ Release の 6 ファイルすべてを同じフォルダーに保存してください：

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

`LocalScreenTranslator_Setup_1.0.0.exe` を実行します。Python、Ollama、PaddlePaddle、CUDA Toolkit、モデルの個別インストールは不要です。

## 要件

Windows 10/11 x64、NVIDIA GPU、Compute Capability 7.5+、8 GB VRAM 推奨、約 10 GB の空き容量。

ゲームでは **Borderless Windowed** を推奨します。

## ダウンロード

[Windows インストーラーと SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

プロジェクトは MIT License。第三者ライセンスは `THIRD_PARTY_NOTICES.md`、`NOTICE`、`third_party_licenses/` を参照してください。
