import json
import os
import subprocess
from pathlib import Path


class AlignClient:
    def __init__(self):
        project_dir = Path(__file__).resolve().parent

        python_exe = (
            project_dir
            / ".venv-align"
            / "Scripts"
            / "python.exe"
        )

        worker_script = project_dir / "align_worker.py"

        creationflags = subprocess.CREATE_NO_WINDOW

        self.process = subprocess.Popen(
        [
        str(python_exe),
        "-X",
        "utf8",
        str(worker_script),
        ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            bufsize=1,
            creationflags=creationflags,
        )

        ready_line = self.process.stdout.readline()

        if not ready_line:
            error = self.process.stderr.read()
            raise RuntimeError(
                f"SimAlign worker failed to start:\n{error}"
            )

        ready = json.loads(ready_line)

        if ready.get("status") != "ready":
            raise RuntimeError(
                f"Unexpected worker response: {ready}"
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

        self.process.stdin.write(
            json.dumps(
                request,
                ensure_ascii=False,
            )
            + "\n"
        )

        self.process.stdin.flush()

        response_line = self.process.stdout.readline()

        if not response_line:
            error = self.process.stderr.read()
            raise RuntimeError(
                f"SimAlign worker stopped:\n{error}"
            )

        response = json.loads(response_line)

        if response.get("status") != "ok":
            raise RuntimeError(
                response.get(
                    "error",
                    "Unknown SimAlign error",
                )
            )

        return response

    def close(self):
        if self.process.poll() is None:
            self.process.terminate()

        try:
            self.process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            self.process.kill()


