from __future__ import annotations

from system_check import CheckResult, FAIL, WARN
from system_check_i18n import (
    current_system_check_language,
    sc_t,
)
from system_check_help_translations import (
    HELP_TRANSLATIONS_EXTRA,
)


def _entry(
    code: str,
    title: str,
    actions: list[str],
    search_terms: str,
) -> dict:
    return {
        "code": code,
        "title": title,
        "actions": actions,
        "search_terms": search_terms,
    }


def help_for_result(result: CheckResult) -> dict | None:
    if result.status not in {FAIL, WARN}:
        return None

    name = result.name
    detail = result.detail.lower()

    if name == "Windows":
        return _entry(
            "LST-SYS-001",
            "Unsupported Windows configuration",
            [
                "Use a 64-bit x86-64 version of Windows 10 or Windows 11.",
                "Install all pending Windows updates.",
                "Restart Windows and run System Check again.",
            ],
            "Windows x64 system type how to check",
        )

    if name in {
        "NVIDIA GPU",
        "Compute capability",
        "GPU requirements",
    }:
        if "driver=" in detail and "required" in detail:
            return _entry(
                "LST-GPU-002",
                "NVIDIA driver is too old",
                [
                    "Download and install the newest NVIDIA driver for your GPU.",
                    "Restart Windows after installing the driver.",
                    "Run System Check again.",
                ],
                "NVIDIA latest driver download update Windows",
            )

        if "compute capability" in detail and "required" in detail:
            return _entry(
                "LST-GPU-003",
                "The NVIDIA GPU is not compatible",
                [
                    "This GPU cannot run the required CUDA/Paddle runtime.",
                    "Use a newer supported NVIDIA GPU.",
                    "Do not install a different CUDA Toolkit manually; the application includes its own runtime.",
                ],
                "NVIDIA GPU compute capability",
            )

        if "vram" in detail and "recommended" in detail:
            return _entry(
                "LST-GPU-004",
                "GPU memory is below the recommended amount",
                [
                    "Close games, browsers and other GPU-heavy applications.",
                    "Run System Check again and check the free VRAM value.",
                    "If translation still fails, use an NVIDIA GPU with more VRAM.",
                ],
                "Windows check GPU VRAM usage NVIDIA",
            )

        return _entry(
            "LST-GPU-001",
            "NVIDIA GPU or driver could not be detected",
            [
                "Open Device Manager and confirm that the NVIDIA GPU is detected without an error icon.",
                "Install or reinstall the official NVIDIA graphics driver.",
                "Restart Windows and run System Check again.",
            ],
            "NVIDIA GPU not detected Windows nvidia-smi",
        )

    if name == "GPU routing":
        return _entry(
            "LST-GPU-010",
            "Multiple NVIDIA GPUs were detected",
            [
                "The current application build uses NVIDIA GPU 0.",
                "Close the application and check which GPU is listed as gpu:0 in this report.",
                "If translation uses the wrong GPU, change the Windows/NVIDIA GPU configuration before trying again.",
            ],
            "NVIDIA multiple GPUs CUDA device 0 Windows",
        )

    if name in {"Capture adapter", "DXcam capture"}:
        return _entry(
            "LST-CAP-001",
            "Screen capture could not use the expected display",
            [
                "Make sure the monitor you want to translate is connected to the NVIDIA GPU.",
                "Try running the game or application in Borderless Windowed mode.",
                "Restart Local Screen Translator after changing monitor connections or display settings.",
                "Run System Check again.",
            ],
            "DXcam screen capture wrong monitor DXGI Windows",
        )

    if name == "Ollama port":
        return _entry(
            "LST-NET-001",
            "Local port 11435 is already used by another program",
            [
                "Close other local AI applications and Ollama instances.",
                "Restart Local Screen Translator.",
                "If the problem remains, restart Windows and run System Check before opening other AI software.",
            ],
            "Windows find process using TCP port 11435 netstat",
        )

    if name == "English TTS":
        return _entry(
            "LST-TTS-001",
            "No usable English Microsoft voice was found",
            [
                "Open Local Screen Translator Settings.",
                "Choose a Microsoft English voice pack.",
                "Click Install Microsoft voice.",
                "Restart Windows if the installation asks for it.",
            ],
            "Windows install text to speech English voice pack",
        )

    if name == "Paddle CUDA":
        return _entry(
            "LST-CUDA-001",
            "GPU OCR could not start",
            [
                "Update or reinstall the NVIDIA graphics driver.",
                "Restart Windows.",
                "Close software that is heavily using GPU memory.",
                "Run System Check again.",
                "Do not install Python, PaddlePaddle or a separate CUDA Toolkit manually.",
            ],
            "PaddlePaddle CUDA GPU initialization failed Windows NVIDIA",
        )

    if name in {
        "Bundled Ollama",
        "Ollama models",
        "Paddle detection model",
        "Paddle recognition model",
        "BERT model",
        "Align worker",
        "Assets root",
    }:
        return _entry(
            "LST-FILE-001",
            "A required application file is missing",
            [
                "Do not download individual model or DLL files manually.",
                "Check Windows Security Protection history in case a file was quarantined.",
                "Uninstall Local Screen Translator.",
                "Install the complete release again with all installer .bin files placed next to the Setup .exe.",
                "Run System Check again.",
            ],
            "Windows Security protection history restore quarantined app file",
        )

    if name == "Align worker runtime":
        return _entry(
            "LST-ALIGN-001",
            "The text alignment component could not start",
            [
                "Check Windows Security Protection history for a blocked or quarantined LSTAlignWorker.exe.",
                "If it was removed, reinstall the complete application.",
                "Restart Windows and run System Check again.",
            ],
            "Windows Security blocked exe Protection history",
        )

    if name == "User data folder":
        return _entry(
            "LST-DATA-001",
            "The application cannot write its settings",
            [
                "Make sure your Windows user account can write to the AppData folder.",
                "Check Controlled Folder Access or other security software.",
                "Do not run the application from a read-only user profile.",
                "Run System Check again.",
            ],
            "Windows AppData permission Controlled Folder Access",
        )

    if name == "Bundled Ollama runtime":
        return _entry(
            "LST-AI-001",
            "The local translation models could not run",
            [
                "Update the NVIDIA driver and restart Windows.",
                "Close other AI applications and GPU-heavy programs.",
                "Check Windows Security Protection history for blocked application files.",
                "If required models are reported missing, reinstall the complete application.",
                "Run System Check again.",
            ],
            "Ollama model failed to load NVIDIA Windows",
        )

    return _entry(
        "LST-GEN-001",
        "System Check found a problem",
        [
            "Restart Windows and run System Check again.",
            "Use the exact error text below as a web search query.",
            "If application files are missing, reinstall the complete application.",
        ],
        f"Local Screen Translator {result.name} {result.detail}",
    )



RU_HELP = {
    "LST-SYS-001": {
        "title": "Неподдерживаемая конфигурация Windows",
        "actions": [
            "Используйте 64-битную версию Windows 10 или Windows 11.",
            "Установите все доступные обновления Windows.",
            "Перезагрузите Windows и снова запустите Проверку системы.",
        ],
    },

    "LST-GPU-001": {
        "title": "Не удалось обнаружить NVIDIA GPU или драйвер",
        "actions": [
            "Откройте Диспетчер устройств и убедитесь, что видеокарта NVIDIA определяется без ошибок.",
            "Установите или переустановите официальный драйвер NVIDIA.",
            "Перезагрузите Windows и снова запустите Проверку системы.",
        ],
    },

    "LST-GPU-002": {
        "title": "Драйвер NVIDIA слишком старый",
        "actions": [
            "Скачайте и установите последнюю версию драйвера NVIDIA для вашей видеокарты.",
            "После установки перезагрузите Windows.",
            "Снова запустите Проверку системы.",
        ],
    },

    "LST-GPU-003": {
        "title": "Видеокарта NVIDIA несовместима",
        "actions": [
            "Эта видеокарта не может запустить требуемую CUDA/Paddle среду.",
            "Используйте более новую совместимую видеокарту NVIDIA.",
            "Не устанавливайте CUDA Toolkit вручную — приложение содержит собственную среду.",
        ],
    },

    "LST-GPU-004": {
        "title": "Недостаточно видеопамяти",
        "actions": [
            "Закройте игры, браузеры и другие программы, активно использующие GPU.",
            "Снова запустите Проверку системы и посмотрите количество свободной VRAM.",
            "Если перевод всё равно не работает, потребуется NVIDIA GPU с большим объёмом памяти.",
        ],
    },

    "LST-GPU-010": {
        "title": "Обнаружено несколько видеокарт NVIDIA",
        "actions": [
            "Текущая версия приложения использует NVIDIA GPU 0.",
            "Посмотрите в технических данных, какая видеокарта указана как gpu:0.",
            "Если используется не та видеокарта, измените настройки GPU в Windows/NVIDIA и перезапустите приложение.",
        ],
    },

    "LST-CAP-001": {
        "title": "Не удалось правильно захватить экран",
        "actions": [
            "Убедитесь, что нужный монитор подключён к видеокарте NVIDIA.",
            "Попробуйте режим игры «Безрамочное окно / Borderless Windowed».",
            "После изменения мониторов или настроек экрана перезапустите Local Screen Translator.",
            "Снова запустите Проверку системы.",
        ],
    },

    "LST-NET-001": {
        "title": "Локальный порт 11435 занят другой программой",
        "actions": [
            "Закройте другие локальные AI-программы и запущенные экземпляры Ollama.",
            "Перезапустите Local Screen Translator.",
            "Если проблема остаётся, перезагрузите Windows и запустите приложение до других AI-программ.",
        ],
    },

    "LST-TTS-001": {
        "title": "Не найден подходящий английский голос Microsoft",
        "actions": [
            "Откройте настройки Local Screen Translator.",
            "Выберите английский голосовой пакет Microsoft.",
            "Нажмите кнопку установки голоса Microsoft.",
            "Если потребуется, перезагрузите Windows.",
        ],
    },

    "LST-CUDA-001": {
        "title": "Не удалось запустить GPU OCR",
        "actions": [
            "Обновите или переустановите драйвер NVIDIA.",
            "Перезагрузите Windows.",
            "Закройте программы, активно использующие видеопамять.",
            "Снова запустите Проверку системы.",
            "Не устанавливайте Python, PaddlePaddle или отдельный CUDA Toolkit вручную.",
        ],
    },

    "LST-FILE-001": {
        "title": "Отсутствует необходимый файл приложения",
        "actions": [
            "Не скачивайте отдельные модели или DLL вручную.",
            "Проверьте журнал защиты Windows Security — файл мог попасть в карантин.",
            "Удалите Local Screen Translator.",
            "Установите приложение заново, положив Setup.exe и все файлы .bin рядом друг с другом.",
            "Снова запустите Проверку системы.",
        ],
    },

    "LST-ALIGN-001": {
        "title": "Не удалось запустить компонент выравнивания текста",
        "actions": [
            "Проверьте журнал защиты Windows Security — LSTAlignWorker.exe мог быть заблокирован.",
            "Если файл был удалён, переустановите приложение полностью.",
            "Перезагрузите Windows и снова запустите Проверку системы.",
        ],
    },

    "LST-DATA-001": {
        "title": "Приложение не может сохранить настройки",
        "actions": [
            "Убедитесь, что ваша учётная запись Windows имеет доступ к папке AppData.",
            "Проверьте Controlled Folder Access и другое защитное ПО.",
            "Снова запустите Проверку системы.",
        ],
    },

    "LST-AI-001": {
        "title": "Не удалось запустить локальные модели перевода",
        "actions": [
            "Обновите драйвер NVIDIA и перезагрузите Windows.",
            "Закройте другие AI-программы и приложения, активно использующие GPU.",
            "Проверьте журнал защиты Windows Security.",
            "Если отсутствуют модели, полностью переустановите приложение.",
            "Снова запустите Проверку системы.",
        ],
    },

    "LST-GEN-001": {
        "title": "Проверка системы обнаружила проблему",
        "actions": [
            "Перезагрузите Windows и снова запустите Проверку системы.",
            "Используйте точный текст ошибки из технических данных для поиска в интернете.",
            "Если отсутствуют файлы приложения, полностью переустановите его.",
        ],
    },
}


HELP_TRANSLATIONS = {
    "ru": RU_HELP,
    **HELP_TRANSLATIONS_EXTRA,
}


def _localize_help_item(item: dict) -> dict:
    language = current_system_check_language()

    translated = (
        HELP_TRANSLATIONS
        .get(language, {})
        .get(item["code"])
    )

    if not translated:
        return item

    result = dict(item)
    result["title"] = translated["title"]
    result["actions"] = translated["actions"]

    return result


def format_self_help_report(
    results: list[CheckResult],
) -> str:
    problems = [
        result
        for result in results
        if result.status in {FAIL, WARN}
    ]

    if not problems:
        return (
            sc_t("report_ready_title")
            + "\n\n"
            + sc_t("report_ready_line1")
            + "\n"
            + sc_t("report_ready_line2")
        )

    lines = [
        sc_t("report_self_help_title"),
        "",
    ]

    for number, result in enumerate(
        problems,
        start=1,
    ):
        help_item = help_for_result(result)
        help_item = _localize_help_item(help_item)

        lines.append(
            f"{number}. [{result.status}] "
            f"{help_item['code']} - {help_item['title']}"
        )
        lines.append(
            f"{sc_t('report_detected')} "
            f"{result.detail}"
        )
        lines.append("")
        lines.append(
            sc_t("report_how_to_fix")
        )

        for index, action in enumerate(
            help_item["actions"],
            start=1,
        ):
            lines.append(
                f"  {index}. {action}"
            )

        lines.append("")
        lines.append(
            sc_t("report_search_web")
        )
        lines.append(
            f'  "{help_item["search_terms"]}"'
        )
        lines.append("")
        lines.append("-" * 60)
        lines.append("")

    lines.append(
        sc_t("report_after_steps")
    )

    return "\n".join(lines)
