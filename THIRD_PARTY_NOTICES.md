# Third-Party Notices

Local Screen Translator contains and redistributes third-party software,
libraries, runtime components and machine-learning models.

These components remain subject to their own licenses. The MIT License covering
Local Screen Translator does not change those third-party terms.

## Translation models

### Qwen3 4B

Component:

`qwen3:4b`

Project:

Qwen3 / Qwen Team, Alibaba Cloud

License:

Apache License 2.0

The bundled Ollama model contains its own Apache 2.0 license layer.

### NVIDIA Riva Translate

Bundled translation model:

`riva-translate:latest`

Source model:

`nvidia/Riva-Translate-4B-Instruct-v2`

Packaged GGUF source:

`liodon-ai/Riva-Translate-4B-Instruct-v2-imatrix-GGUF`

Governing terms:

NVIDIA Open Model License Agreement.

Required NVIDIA attribution is also present in the repository `NOTICE` file.

A copy of the applicable NVIDIA agreement is stored under:

`third_party_licenses/models/NVIDIA_Open_Model_License_Agreement_2025-10-24.pdf`

NVIDIA also identifies Apache License 2.0 as additional information for the
Riva-Translate-4B-Instruct-v2 model.

### Multilingual BERT

Component:

`google-bert/bert-base-multilingual-cased`

Used by the alignment pipeline.

License:

Apache License 2.0

## Local AI runtime

### Ollama

The application redistributes an Ollama runtime used only as a local model
server.

License:

MIT License

A copy of the Ollama license is included under:

`third_party_licenses/ollama/`

## Python runtime

The standalone application contains a CPython 3.12 runtime.

Python is distributed under the Python Software Foundation License and related
notices.

A copy of the CPython 3.12.10 license is included under:

`third_party_licenses/python-runtime/`

## Major Python components

The application uses components including:

- PySide6 / Qt for the graphical interface
- PaddlePaddle GPU
- PaddleOCR
- PaddleX
- DXcam
- NumPy
- OpenCV
- Requests
- Python/WinRT
- comtypes
- SimAlign
- PyTorch
- Transformers
- Tokenizers

Their original license files found in the installed Python distributions are
collected under:

`third_party_licenses/python-packages/`

This directory may also contain licenses for transitive dependencies included
in the frozen application.

## PySide6 / Qt

PySide6 package metadata identifies licensing options including LGPL-3.0-only
and GPL alternatives.

Local Screen Translator does not claim ownership of Qt or PySide6.

Their applicable notices and license files are included with the collected
third-party package licenses.

## NVIDIA runtime libraries

Some Python and GPU packages may redistribute NVIDIA runtime libraries.

Their applicable NVIDIA license/EULA files, when shipped with the installed
Python package distributions, are preserved under the collected
`third_party_licenses/python-packages/` directory.

## No relicensing

Names, trademarks, model weights, third-party libraries and other separately
licensed components remain the property of their respective owners.

For the exact terms governing a component, refer to the corresponding license
file and upstream project documentation.
