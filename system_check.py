from __future__ import annotations

import os
import platform
import shutil
import socket
import subprocess
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import requests

from config import SETTINGS
from runtime_paths import (
    ALIGN_WORKER_EXE,
    ASSETS_ROOT,
    BERT_MODEL_DIR,
    OLLAMA_EXE,
    OLLAMA_MODELS_DIR,
    PADDLE_DET_MODEL_DIR,
    PADDLE_REC_MODEL_DIR,
)


PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str


def _path_check(
    name: str,
    path: Path,
    *,
    directory: bool = False,
) -> CheckResult:
    exists = path.is_dir() if directory else path.is_file()

    return CheckResult(
        name,
        PASS if exists else FAIL,
        str(path) if exists else f"Missing: {path}",
    )


def check_windows() -> CheckResult:
    machine = platform.machine()

    if os.name != "nt":
        return CheckResult(
            "Windows",
            FAIL,
            f"Unsupported OS: {platform.platform()}",
        )

    if machine.lower() not in {"amd64", "x86_64"}:
        return CheckResult(
            "Windows",
            FAIL,
            f"64-bit Windows required; architecture={machine}",
        )

    return CheckResult(
        "Windows",
        PASS,
        f"{platform.platform()} | architecture={machine}",
    )


def _find_nvidia_smi() -> str | None:
    found = shutil.which("nvidia-smi")

    if found:
        return found

    candidates = (
        Path(os.environ.get("WINDIR", r"C:\Windows"))
        / "System32"
        / "nvidia-smi.exe",
        Path(r"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe"),
    )

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return None


def check_nvidia() -> CheckResult:
    exe = _find_nvidia_smi()

    if not exe:
        return CheckResult(
            "NVIDIA GPU",
            FAIL,
            "nvidia-smi was not found",
        )

    command = [
        exe,
        "--query-gpu=name,driver_version,memory.total,memory.free",
        "--format=csv,noheader,nounits",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=8,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            ),
            check=False,
        )
    except Exception as exc:
        return CheckResult(
            "NVIDIA GPU",
            FAIL,
            f"nvidia-smi failed: {exc}",
        )

    if result.returncode != 0:
        error = (
            result.stderr.strip()
            or result.stdout.strip()
            or f"exit code {result.returncode}"
        )

        return CheckResult(
            "NVIDIA GPU",
            FAIL,
            error,
        )

    gpus = []

    for index, line in enumerate(
        result.stdout.splitlines()
    ):
        parts = [
            part.strip()
            for part in line.split(",")
        ]

        if len(parts) < 4:
            continue

        name, driver, total, free = parts[:4]

        gpus.append(
            f"GPU {index}: {name} | "
            f"driver={driver} | "
            f"VRAM={total} MB | "
            f"free={free} MB"
        )

    if not gpus:
        return CheckResult(
            "NVIDIA GPU",
            FAIL,
            "No NVIDIA GPU returned by nvidia-smi",
        )

    return CheckResult(
        "NVIDIA GPU",
        PASS,
        " ; ".join(gpus),
    )


def check_compute_capability() -> CheckResult:
    exe = _find_nvidia_smi()

    if not exe:
        return CheckResult(
            "Compute capability",
            WARN,
            "Cannot query without nvidia-smi",
        )

    try:
        result = subprocess.run(
            [
                exe,
                "--query-gpu=name,compute_cap",
                "--format=csv,noheader",
            ],
            capture_output=True,
            text=True,
            timeout=8,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            ),
            check=False,
        )

        if result.returncode != 0:
            return CheckResult(
                "Compute capability",
                WARN,
                "Driver does not expose compute_cap query",
            )

        text = " ; ".join(
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        )

        return CheckResult(
            "Compute capability",
            PASS,
            text or "Detected",
        )

    except Exception as exc:
        return CheckResult(
            "Compute capability",
            WARN,
            str(exc),
        )



MIN_NVIDIA_DRIVER_MAJOR = 580
MIN_COMPUTE_CAPABILITY = 7.5
RECOMMENDED_VRAM_MB = 8192


def check_hardware_requirements() -> CheckResult:
    exe = _find_nvidia_smi()

    if not exe:
        return CheckResult(
            "GPU requirements",
            FAIL,
            "NVIDIA GPU / nvidia-smi was not found",
        )

    try:
        result = subprocess.run(
            [
                exe,
                "--query-gpu=index,name,driver_version,"
                "memory.total,memory.free,compute_cap",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=8,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            ),
            check=False,
        )

        if result.returncode != 0:
            return CheckResult(
                "GPU requirements",
                WARN,
                "Could not query all GPU compatibility fields",
            )

        rows = []

        for line in result.stdout.splitlines():
            parts = [
                part.strip()
                for part in line.split(",")
            ]

            if len(parts) != 6:
                continue

            try:
                rows.append(
                    {
                        "index": int(parts[0]),
                        "name": parts[1],
                        "driver": parts[2],
                        "total": int(parts[3]),
                        "free": int(parts[4]),
                        "compute": float(parts[5]),
                    }
                )
            except ValueError:
                continue

        if not rows:
            return CheckResult(
                "GPU requirements",
                FAIL,
                "No usable NVIDIA GPU information returned",
            )

        rows.sort(
            key=lambda item: item["index"]
        )

        # Current application configuration uses Paddle gpu:0.
        gpu = rows[0]

        try:
            driver_major = int(
                gpu["driver"].split(".", 1)[0]
            )
        except ValueError:
            driver_major = 0

        if driver_major < MIN_NVIDIA_DRIVER_MAJOR:
            return CheckResult(
                "GPU requirements",
                FAIL,
                f"{gpu['name']} | "
                f"driver={gpu['driver']} "
                f"(required {MIN_NVIDIA_DRIVER_MAJOR}+) | "
                f"Compute Capability={gpu['compute']} | "
                f"VRAM={gpu['total']} MB",
            )

        if gpu["compute"] <= MIN_COMPUTE_CAPABILITY:
            return CheckResult(
                "GPU requirements",
                FAIL,
                f"{gpu['name']} | "
                f"Compute Capability={gpu['compute']} "
                f"(required >{MIN_COMPUTE_CAPABILITY})",
            )

        detail = (
            f"gpu:0={gpu['name']} | "
            f"driver={gpu['driver']} | "
            f"Compute Capability={gpu['compute']} | "
            f"VRAM={gpu['total']} MB | "
            f"free={gpu['free']} MB"
        )

        if gpu["total"] < RECOMMENDED_VRAM_MB:
            return CheckResult(
                "GPU requirements",
                WARN,
                detail
                + f" | recommended VRAM >= "
                f"{RECOMMENDED_VRAM_MB} MB",
            )

        return CheckResult(
            "GPU requirements",
            PASS,
            detail,
        )

    except Exception as exc:
        return CheckResult(
            "GPU requirements",
            FAIL,
            f"Hardware compatibility query failed: {exc}",
        )


def check_gpu_routing() -> CheckResult:
    exe = _find_nvidia_smi()

    if not exe:
        return CheckResult(
            "GPU routing",
            FAIL,
            "NVIDIA GPU information unavailable",
        )

    try:
        result = subprocess.run(
            [
                exe,
                "--query-gpu=index,name",
                "--format=csv,noheader",
            ],
            capture_output=True,
            text=True,
            timeout=8,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            ),
            check=False,
        )

        names = [
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        if not names:
            return CheckResult(
                "GPU routing",
                FAIL,
                "No NVIDIA GPUs detected",
            )

        if len(names) == 1:
            return CheckResult(
                "GPU routing",
                PASS,
                f"Single NVIDIA GPU detected: {names[0]}",
            )

        return CheckResult(
            "GPU routing",
            WARN,
            f"{len(names)} NVIDIA GPUs detected: "
            + " ; ".join(names)
            + " | current build uses Paddle gpu:0; "
            "manual GPU selection is not implemented yet",
        )

    except Exception as exc:
        return CheckResult(
            "GPU routing",
            WARN,
            f"GPU routing check failed: {exc}",
        )


def check_dxcam_routing() -> CheckResult:
    try:
        import dxcam

        info = str(
            dxcam.device_info()
        )

        count = info.count("Device[")

        if count <= 1:
            return CheckResult(
                "Capture adapter",
                PASS,
                "DXcam device 0 is the only detected adapter",
            )

        return CheckResult(
            "Capture adapter",
            WARN,
            f"DXcam detected {count} adapters | "
            f"current configuration uses device "
            f"{SETTINGS.capture_device_idx}",
        )

    except Exception as exc:
        return CheckResult(
            "Capture adapter",
            WARN,
            f"Adapter enumeration failed: {exc}",
        )

def check_ollama_port() -> CheckResult:
    parsed = urlparse(SETTINGS.ollama_url)

    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 11435

    try:
        with socket.create_connection(
            (host, port),
            timeout=0.4,
        ):
            occupied = True

    except OSError:
        occupied = False

    if not occupied:
        return CheckResult(
            "Ollama port",
            PASS,
            f"{host}:{port} is available",
        )

    try:
        response = requests.get(
            f"{SETTINGS.ollama_url.rstrip('/')}/api/version",
            timeout=1.5,
        )

        data = response.json()

        if (
            response.ok
            and isinstance(data, dict)
            and data.get("version")
        ):
            return CheckResult(
                "Ollama port",
                PASS,
                f"Ollama server is ready on {host}:{port}; "
                f"version={data['version']}",
            )

    except Exception:
        pass

    return CheckResult(
        "Ollama port",
        FAIL,
        f"{host}:{port} is occupied by an unknown service",
    )


def check_tts() -> CheckResult:
    try:
        from speech import get_installed_english_voices

        voices = get_installed_english_voices()

        if not voices:
            return CheckResult(
                "English TTS",
                WARN,
                "No English Microsoft speech voices detected",
            )

        names = []

        for voice in voices:
            if isinstance(voice, dict):
                name = voice.get("name", "Unknown")
                language = voice.get("language", "")
            else:
                name = getattr(voice, "name", str(voice))
                language = getattr(voice, "language", "")

            names.append(
                f"{name} ({language})"
                if language
                else name
            )

        return CheckResult(
            "English TTS",
            PASS,
            " ; ".join(names),
        )

    except Exception as exc:
        return CheckResult(
            "English TTS",
            WARN,
            f"TTS check failed: {exc}",
        )



def check_paddle_cuda() -> CheckResult:
    try:
        import paddle

        if not paddle.device.is_compiled_with_cuda():
            return CheckResult(
                "Paddle CUDA",
                FAIL,
                "Paddle was built without CUDA support",
            )

        count = paddle.device.cuda.device_count()

        if count < 1:
            return CheckResult(
                "Paddle CUDA",
                FAIL,
                "No CUDA device is available to Paddle",
            )

        # Do not create tensors here.
        # Tensor execution mode can differ between background threads.
        # Query and synchronize the CUDA device directly instead.
        device_name = paddle.device.cuda.get_device_name(0)

        paddle.device.set_device("gpu:0")
        current = paddle.device.get_device()

        paddle.device.synchronize("gpu:0")

        if current != "gpu:0":
            return CheckResult(
                "Paddle CUDA",
                FAIL,
                f"Expected gpu:0, current device is {current}",
            )

        return CheckResult(
            "Paddle CUDA",
            PASS,
            f"Paddle {paddle.__version__} | "
            f"CUDA devices={count} | "
            f"gpu:0={device_name} | "
            f"current={current} | "
            "CUDA synchronization OK",
        )

    except Exception as exc:
        return CheckResult(
            "Paddle CUDA",
            FAIL,
            f"CUDA runtime test failed: {exc}",
        )


def check_dxcam_capture() -> CheckResult:
    try:
        import dxcam

        camera = dxcam.create(
            device_idx=SETTINGS.capture_device_idx,
            output_idx=SETTINGS.capture_output_idx,
            output_color="BGRA",
            backend=SETTINGS.capture_backend,
            processor_backend="numpy",
        )

        frame = camera.grab()

        if frame is None:
            return CheckResult(
                "DXcam capture",
                WARN,
                "DXcam initialized, but one-shot capture returned no frame",
            )

        height, width = frame.shape[:2]

        return CheckResult(
            "DXcam capture",
            PASS,
            f"Captured {width}x{height} frame | "
            f"device={SETTINGS.capture_device_idx} | "
            f"output={SETTINGS.capture_output_idx}",
        )

    except Exception as exc:
        return CheckResult(
            "DXcam capture",
            FAIL,
            f"Screen capture test failed: {exc}",
        )


def check_align_worker_startup() -> CheckResult:
    client = None

    try:
        from align_client import AlignClient

        client = AlignClient()

        return CheckResult(
            "Align worker runtime",
            PASS,
            "Worker started and loaded the bundled BERT model",
        )

    except Exception as exc:
        return CheckResult(
            "Align worker runtime",
            FAIL,
            f"Worker startup failed: {exc}",
        )

    finally:
        if client is not None:
            try:
                client.close()
            except Exception:
                pass


def check_user_data_write() -> CheckResult:
    try:
        from user_settings import APP_DIR

        directory = Path(APP_DIR)
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        test_file = (
            directory
            / f".system_check_{os.getpid()}.tmp"
        )

        payload = "Local Screen Translator write test"

        test_file.write_text(
            payload,
            encoding="utf-8",
        )

        if test_file.read_text(
            encoding="utf-8",
        ) != payload:
            raise RuntimeError(
                "Written test data could not be read back correctly"
            )

        test_file.unlink()

        return CheckResult(
            "User data folder",
            PASS,
            f"Writable: {directory}",
        )

    except Exception as exc:
        return CheckResult(
            "User data folder",
            FAIL,
            f"Write test failed: {exc}",
        )

def run_basic_system_check() -> list[CheckResult]:
    return [
        check_windows(),
        check_nvidia(),
        check_compute_capability(),
        check_hardware_requirements(),
        check_gpu_routing(),
        check_dxcam_routing(),

        CheckResult(
            "Assets root",
            PASS if ASSETS_ROOT.is_dir() else FAIL,
            str(ASSETS_ROOT),
        ),

        _path_check(
            "Bundled Ollama",
            OLLAMA_EXE,
        ),

        _path_check(
            "Ollama models",
            OLLAMA_MODELS_DIR,
            directory=True,
        ),

        _path_check(
            "Paddle detection model",
            PADDLE_DET_MODEL_DIR,
            directory=True,
        ),

        _path_check(
            "Paddle recognition model",
            PADDLE_REC_MODEL_DIR,
            directory=True,
        ),

        _path_check(
            "BERT model",
            BERT_MODEL_DIR,
            directory=True,
        ),

        _path_check(
            "Align worker",
            ALIGN_WORKER_EXE,
        ),

        check_ollama_port(),
        check_tts(),
    ]


def format_report(
    results: list[CheckResult],
) -> str:
    lines = [
        "=== LOCAL SCREEN TRANSLATOR SYSTEM CHECK ===",
        "",
    ]

    for result in results:
        lines.append(
            f"[{result.status}] "
            f"{result.name}: {result.detail}"
        )

    statuses = {
        result.status
        for result in results
    }

    if FAIL in statuses:
        overall = FAIL
    elif WARN in statuses:
        overall = WARN
    else:
        overall = PASS

    lines.extend(
        [
            "",
            f"OVERALL: {overall}",
        ]
    )

    return "\n".join(lines)



def check_bundled_ollama_runtime() -> CheckResult:
    host = SETTINGS.ollama_url.rstrip("/")
    parsed = urlparse(host)

    hostname = parsed.hostname or "127.0.0.1"
    port = parsed.port or 11435

    process = None

    def verify_server() -> CheckResult:
        try:
            version_response = requests.get(
                host + "/api/version",
                timeout=3,
            )
            version_response.raise_for_status()

            version = version_response.json().get(
                "version",
                "unknown",
            )

            tags_response = requests.get(
                host + "/api/tags",
                timeout=5,
            )
            tags_response.raise_for_status()

            models = {
                item.get("name", "")
                for item in tags_response.json().get(
                    "models",
                    [],
                )
            }

            required = {
                "qwen3:4b",
                "riva-translate:latest",
            }

            missing = required - models

            if missing:
                return CheckResult(
                    "Bundled Ollama runtime",
                    FAIL,
                    "Missing required models: "
                    + ", ".join(sorted(missing)),
                )

            qwen = requests.post(
                host + "/api/chat",
                json={
                    "model": "qwen3:4b",
                    "messages": [
                        {
                            "role": "user",
                            "content": "Write one short English word.",
                        }
                    ],
                    "stream": False,
                    "think": False,
                    "keep_alive": 0,
                    "options": {
                        "temperature": 0,
                        "num_predict": 16,
                    },
                },
                timeout=60,
            )

            qwen.raise_for_status()

            if not (
                qwen.json()
                .get("message", {})
                .get("content", "")
                .strip()
            ):
                raise RuntimeError(
                    "Qwen returned an empty response"
                )

            riva = requests.post(
                host + "/api/generate",
                json={
                    "model": "riva-translate:latest",
                    "prompt": (
                        "Translate into Russian: "
                        "The door is open."
                    ),
                    "stream": False,
                    "keep_alive": 0,
                },
                timeout=60,
            )

            riva.raise_for_status()

            if not riva.json().get(
                "response",
                "",
            ).strip():
                raise RuntimeError(
                    "Riva returned an empty response"
                )

            return CheckResult(
                "Bundled Ollama runtime",
                PASS,
                f"Ollama {version} | "
                "qwen3:4b inference OK | "
                "riva-translate inference OK",
            )

        except Exception as exc:
            return CheckResult(
                "Bundled Ollama runtime",
                FAIL,
                f"Runtime test failed: {exc}",
            )

    try:
        with socket.create_connection(
            (hostname, port),
            timeout=0.3,
        ):
            return verify_server()

    except OSError:
        pass

    env = os.environ.copy()
    env["OLLAMA_HOST"] = f"{hostname}:{port}"
    env["OLLAMA_MODELS"] = str(OLLAMA_MODELS_DIR)

    try:
        process = subprocess.Popen(
            [str(OLLAMA_EXE), "serve"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=getattr(
                subprocess,
                "CREATE_NO_WINDOW",
                0,
            ),
            env=env,
        )

        import time

        deadline = time.monotonic() + 15.0

        while time.monotonic() < deadline:
            if process.poll() is not None:
                return CheckResult(
                    "Bundled Ollama runtime",
                    FAIL,
                    f"Ollama exited with code {process.returncode}",
                )

            try:
                response = requests.get(
                    host + "/api/version",
                    timeout=1,
                )

                if response.ok:
                    return verify_server()

            except Exception:
                pass

            time.sleep(0.25)

        return CheckResult(
            "Bundled Ollama runtime",
            FAIL,
            "Bundled Ollama did not start within 15 seconds",
        )

    finally:
        if process is not None:
            try:
                subprocess.run(
                    [
                        "taskkill",
                        "/F",
                        "/T",
                        "/PID",
                        str(process.pid),
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=getattr(
                        subprocess,
                        "CREATE_NO_WINDOW",
                        0,
                    ),
                    timeout=5,
                    check=False,
                )
            except Exception:
                pass


def run_deep_system_check() -> list[CheckResult]:
    results = run_basic_system_check()

    results.extend(
        [
            check_paddle_cuda(),
            check_dxcam_capture(),
            check_align_worker_startup(),
            check_user_data_write(),
            check_bundled_ollama_runtime(),
        ]
    )

    return results


if __name__ == "__main__":
    print(
        format_report(
            run_deep_system_check()
        )
    )
