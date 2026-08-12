@echo off
setlocal
cd /d "%~dp0"

py -3.12 -m venv .venv
if errorlevel 1 (
    echo Python 3.12 was not found. Install 64-bit Python 3.12 and run again.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Python environment is ready.
echo Next:
echo   1. Install/launch Ollama.
echo   2. Configure RTX 3070 Ti with configure_ollama_3070ti.ps1.
echo   3. ollama pull qwen3:4b-instruct
echo   4. Run run.bat
pause
