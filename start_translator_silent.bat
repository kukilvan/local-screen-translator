@echo off
cd /d "%~dp0"

set "OLLAMA_EXE=%LOCALAPPDATA%\Programs\Ollama\ollama.exe"

netstat -ano | findstr ":11434" | findstr "LISTENING" >nul

if errorlevel 1 (
    if not exist "%OLLAMA_EXE%" (
        exit /b 1
    )

    powershell -NoProfile -WindowStyle Hidden -Command "Start-Process -FilePath '%OLLAMA_EXE%' -ArgumentList 'serve' -WindowStyle Hidden"

    timeout /t 2 /nobreak >nul
)

start "" ".venv\Scripts\pythonw.exe" app.py