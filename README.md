# Local Screen Translator (Windows)

Локальный прототип утилиты в стиле Lookupper:

- `Ctrl + Alt + Space` — слово под курсором + окружающий контекст.
- `Ctrl + Alt + Shift + Space` — абзац/блок текста рядом с курсором.
- DXGI one-shot screen capture через DXcam.
- Windows.Media.Ocr на CPU.
- локальная Ollama по `127.0.0.1:11434`.
- popup HUD поверх обычных окон и Borderless Fullscreen.
- HUD не забирает фокус и пропускает клики в игру.
- никакого внешнего API.

## Почему так

### Захват
DXcam использует Desktop Duplication API. В этом проекте `camera.start()` НЕ вызывается:
кадр снимается только при горячей клавише, поэтому в idle нет постоянного capture loop.

### OCR
Используется встроенный Windows OCR. Он возвращает линии, отдельные слова и bounding boxes,
поэтому можно определить слово непосредственно под курсором.

### LLM
По умолчанию:
`qwen3:4b-instruct`

Для коротких переводов на RTX 3070 Ti 8GB это разумнее 7B/8B модели по задержке.
Если захочется больше качества, можно заменить в `config.py` модель на более крупную.

---

# 1. Требования

- Windows 11 / Windows 10 x64.
- Python 3.12 x64.
- NVIDIA driver, в котором видны обе GPU.
- Ollama for Windows.
- установленный English OCR language capability Windows.

---

# 2. Python

Запусти:

```bat
setup.bat
```

Или вручную:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

---

# 3. Windows OCR

Открой PowerShell **от администратора** и выполни:

```powershell
.\install_ocr_en.ps1
```

Вручную это та же команда:

```powershell
Add-WindowsCapability -Online -Name "Language.OCR~~~en-US~0.0.1.0"
```

Для другого исходного языка поменяй `ocr_language` в `config.py` и установи
соответствующий Windows OCR language capability.

---

# 4. Жестко назначить Ollama на RTX 3070 Ti

Сначала посмотри GPU:

```powershell
nvidia-smi -L
```

Затем:

```powershell
.\configure_ollama_3070ti.ps1
```

Скрипт сам ищет `RTX 3070 Ti`, берет ее UUID и записывает для пользователя:

- `CUDA_VISIBLE_DEVICES=<UUID RTX 3070 Ti>`
- `OLLAMA_NO_CLOUD=1`
- `OLLAMA_HOST=127.0.0.1:11434`
- `OLLAMA_NUM_PARALLEL=1`
- `OLLAMA_MAX_LOADED_MODELS=1`
- `OLLAMA_CONTEXT_LENGTH=2048`

После скрипта ОБЯЗАТЕЛЬНО полностью выбери **Quit Ollama** из системного трея
и запусти Ollama снова — Windows-приложение читает environment variables при старте.

---

# 5. Модель

```powershell
ollama pull qwen3:4b-instruct
```

Проверка:

```powershell
ollama run qwen3:4b-instruct "Translate 'shelter' to Russian. Answer briefly."
```

Затем:

```powershell
ollama ps
```

Также открой:

```powershell
nvidia-smi
```

и убедись, что VRAM у процесса Ollama занята именно на RTX 3070 Ti.

---

# 6. Запуск

```bat
run.bat
```

Горячие клавиши:

- `Ctrl + Alt + Space` — перевод слова.
- `Ctrl + Alt + Shift + Space` — перевод абзаца.

Они находятся в `config.py`.

Важно: `RegisterHotKey` не позволяет нормально использовать комбинацию,
состоящую только из `Ctrl + Alt` без обычной клавиши. Поэтому в MVP используется Space.

---

# 7. Если игра не на основном мониторе

Выполни:

```powershell
.\.venv\Scripts\python.exe -c "import dxcam; print(dxcam.device_info()); print(dxcam.output_info())"
```

Ты увидишь что-то вроде:

```text
Device[0]: ...
Device[0] Output[0]: Res:(2560, 1440) Rot:0 Primary:True
Device[0] Output[1]: Res:(3840, 2160) Rot:0 Primary:False
```

Поменяй в `config.py`:

```python
capture_device_idx = 0
capture_output_idx = 1
```

И перезапусти приложение.

---

# 8. Borderless vs Exclusive Fullscreen

Это принципиальное ограничение Windows:

- обычные приложения: да;
- Borderless Fullscreen: да;
- большинство современных flip-model игр: обычно да;
- настоящий Exclusive Fullscreen: захват DXGI может работать, но обычное top-level
  Qt/Win32 окно не обязано рисоваться поверх swap chain игры.

Для надежной работы HUD без инжекта используй **Borderless Fullscreen**.

Чтобы гарантированно рисовать поверх настоящего Exclusive Fullscreen, нужен уже
другой уровень реализации: DirectX Present hook / injected overlay / game-specific
overlay. Это повышает сложность и может конфликтовать с anti-cheat, поэтому такой
вариант намеренно не используется в этом MVP.

---

# 9. Производительность

Idle:
- нет OCR;
- нет постоянного screenshot loop;
- нет polling клавиатуры: Windows блокирует поток на `GetMessage`;
- HUD timers остановлены, пока окно скрыто;
- модель может оставаться в VRAM, но GPU compute практически не используется.

По hotkey:
1. one-shot DXGI crop;
2. Windows OCR;
3. короткий локальный prompt;
4. ответ Ollama;
5. HUD.

Для самой низкой задержки модель держится в VRAM через `keep_alive=-1`.
Если хочешь освобождать VRAM, в `config.py` поставь, например:

```python
ollama_keep_alive = "10m"
```

---

# 10. Что улучшать дальше

После проверки MVP логичные улучшения:

1. кешировать перевод часто встречающихся слов;
2. автоматически определять OCR-язык;
3. режим удержания клавиши + hover;
4. drag-select прямоугольником;
5. потоковый вывод токенов в HUD;
6. custom glossary для конкретной игры;
7. SQLite-история изученных слов;
8. packaging через PyInstaller/Nuitka в один EXE;
9. отдельный быстрый OCR pipeline для очень мелких игровых шрифтов.
