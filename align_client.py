import json
import os
import subprocess
from pathlib import Path

from runtime_paths import ALIGN_WORKER_EXE, BERT_MODEL_DIR


class AlignClient:
    def __init__(self):
        project_dir = Path(__file__).resolve().parent

        if not BERT_MODEL_DIR.is_dir():
            raise RuntimeError(
                f"LST-FILE-001: Bundled BERT model not found: {BERT_MODEL_DIR}"
            )

        # Release path: prefer the standalone PyInstaller worker.
        if ALIGN_WORKER_EXE.is_file():
            command = [str(ALIGN_WORKER_EXE)]
            worker_description = str(ALIGN_WORKER_EXE)
        else:
            # Development fallback so the source tree remains usable even
            # before a release worker has been built/copied.
            python_exe = (
                project_dir
                / ".venv-align"
                / "Scripts"
                / "python.exe"
            )
            worker_script = project_dir / "align_worker.py"

            if not python_exe.is_file():
                raise RuntimeError(
                    "LST-ALIGN-001: SimAlign runtime not found. "
                    f"Expected standalone worker at {ALIGN_WORKER_EXE} "
                    f"or development Python at {python_exe}"
                )

            if not worker_script.is_file():
                raise RuntimeError(
                    f"LST-ALIGN-001: SimAlign worker script not found: {worker_script}"
                )

            command = [
                str(python_exe),
                "-X",
                "utf8",
                str(worker_script),
            ]
            worker_description = str(worker_script)

        creationflags = subprocess.CREATE_NO_WINDOW

        worker_env = os.environ.copy()
        worker_env["LST_BERT_MODEL_DIR"] = str(BERT_MODEL_DIR)
        worker_env["HF_HUB_OFFLINE"] = "1"
        worker_env["TRANSFORMERS_OFFLINE"] = "1"
        worker_env["HF_DATASETS_OFFLINE"] = "1"

        # The standalone EXE cannot receive Python's "-X utf8" switch.
        # Force UTF-8 explicitly so Russian text in the JSON pipe is preserved.
        worker_env["PYTHONUTF8"] = "1"
        worker_env["PYTHONIOENCODING"] = "utf-8"

        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="strict",
            bufsize=1,
            creationflags=creationflags,
            env=worker_env,
        )

        ready_line = self.process.stdout.readline()

        if not ready_line:
            error = self.process.stderr.read()
            raise RuntimeError(
                "LST-ALIGN-001: SimAlign worker failed to start.\n"
                f"Worker: {worker_description}\n"
                f"{error}"
            )

        try:
            ready = json.loads(ready_line)
        except (json.JSONDecodeError, TypeError) as exc:
            raise RuntimeError(
                "LST-ALIGN-001: SimAlign worker returned invalid "
                f"startup JSON: {ready_line!r}"
            ) from exc

        if ready.get("status") != "ready":
            raise RuntimeError(
                f"LST-ALIGN-001: Unexpected SimAlign startup response: {ready}"
            )

    def align(
        self,
        src,
        trg,
        target_index,
    ):
        request = {
            "src": src,
            "trg": trg,
            "target_index": target_index,
        }

        try:
            self.process.stdin.write(
                json.dumps(
                    request,
                    ensure_ascii=True,
                )
                + "\n"
            )

            self.process.stdin.flush()

        except (BrokenPipeError, OSError, ValueError) as exc:
            raise RuntimeError(
                "LST-ALIGN-001: Could not send a request to "
                f"the SimAlign worker: {exc}"
            ) from exc

        response_line = self.process.stdout.readline()

        if not response_line:
            error = self.process.stderr.read()
            raise RuntimeError(
                f"LST-ALIGN-001: SimAlign worker stopped:\n{error}"
            )

        try:
            response = json.loads(response_line)
        except (json.JSONDecodeError, TypeError) as exc:
            raise RuntimeError(
                "LST-ALIGN-001: SimAlign worker returned invalid "
                f"response JSON: {response_line!r}"
            ) from exc

        if response.get("status") != "ok":
            worker_error = response.get(
                "error",
                "Unknown SimAlign error",
            )

            raise RuntimeError(
                "LST-ALIGN-001: SimAlign worker error: "
                f"{worker_error}"
            )

        return response

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()

        try:
            self.process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            self.process.kill()

