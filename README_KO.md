# Local Screen Translator

**Windows용 오프라인 화면 번역기, 게임 번역기 및 OCR 번역 도구.**  
게임, 애플리케이션, 브라우저와 비디오의 텍스트를 직접 번역합니다. OCR과 번역은 PC에서 로컬로 실행되며 클라우드 번역 API를 사용하지 않습니다.

**버전: 1.0.0**

[English](README.md) | [Русский](README_RU.md) | [Українська](README_UK.md) | [Deutsch](README_DE.md) | [Français](README_FR.md) | [Español](README_ES.md) | [Português](README_PT-BR.md) | [Polski](README_PL.md) | [简体中文](README_ZH-CN.md) | [日本語](README_JA.md) | 한국어

## 주요 기능

- 문맥을 고려한 커서 아래 단어 번역;
- 문단 번역;
- 전역 단축키;
- Borderless Fullscreen 위의 HUD;
- GPU 가속 PaddleOCR;
- 로컬 `qwen3:4b` 및 Riva Translate;
- System Check;
- 다국어 UI.

## 개인정보 보호

번역은 로컬로 수행됩니다. 포함된 Ollama는 `127.0.0.1:11435`를 사용합니다.

## 설치

동일한 Release의 6개 파일을 모두 같은 폴더에 저장하십시오:

- `LocalScreenTranslator_Setup_1.0.0.exe`
- `LocalScreenTranslator_Setup_1.0.0-1.bin`
- `LocalScreenTranslator_Setup_1.0.0-2.bin`
- `LocalScreenTranslator_Setup_1.0.0-3.bin`
- `LocalScreenTranslator_Setup_1.0.0-4.bin`
- `LocalScreenTranslator_Setup_1.0.0-5.bin`

`LocalScreenTranslator_Setup_1.0.0.exe`를 실행합니다. Python, Ollama, PaddlePaddle, CUDA Toolkit 또는 모델을 별도로 설치할 필요가 없습니다.

## 요구 사항

Windows 10/11 x64, NVIDIA GPU, Compute Capability 7.5+, 8 GB VRAM 권장, 약 10 GB 공간.

게임에서는 **Borderless Windowed** 사용을 권장합니다.

## 다운로드

[Windows 설치 프로그램 및 SHA-256 — Releases](https://github.com/kukilvan/local-screen-translator/releases)

프로젝트 라이선스는 MIT입니다. 타사 라이선스: `THIRD_PARTY_NOTICES.md`, `NOTICE`, `third_party_licenses/`.
