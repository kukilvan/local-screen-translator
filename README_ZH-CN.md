# Local Screen Translator

**适用于 Windows 的离线屏幕翻译器、游戏翻译器和 OCR 翻译工具。**  
可直接翻译游戏、应用、浏览器和视频画面中的文字。OCR 与翻译都在本地电脑执行，不依赖云端翻译 API。

**版本：1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | 简体中文 | [日本語](README_JA.md) | [한국어](README_KO.md)

## 主要功能

- 根据上下文翻译鼠标下的单词；
- 翻译附近段落；
- 全局快捷键；
- Borderless Fullscreen 上的 HUD；
- GPU 加速 PaddleOCR；
- 本地 `qwen3:4b` 与 Riva Translate；
- 内置 System Check；
- 多语言界面。

## 隐私

翻译在本地完成。内置 Ollama 使用 `127.0.0.1:11435`。

## 安装

下载同一 Release 的全部六个文件，并放在同一文件夹：

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

运行 `LocalScreenTranslator_Setup_1.0.0.exe`。无需单独安装 Python、Ollama、PaddlePaddle、CUDA Toolkit 或模型。

## 系统要求

Windows 10/11 x64、NVIDIA GPU、Compute Capability 7.5+，建议 8 GB VRAM，安装约需 10 GB 空间。

游戏中建议使用 **Borderless Windowed**。

## 下载

[Windows 安装程序与 SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

项目采用 MIT License。第三方许可证：`THIRD_PARTY_NOTICES.md`、`NOTICE`、`third_party_licenses/`。
