@echo off
cd /d "%~dp0"

set "OLLAMA_EXE=%LOCALAPPDATA%\Programs\Ollama\ollama.exe"

netstat -ano | findstr ":11434" | findstr "LISTENING" >nul

if errorlevel 1 (
    if not exist "%OLLAMA_EXE%" (
        echo Ollama not found:
        echo %OLLAMA_EXE%
        pause
        exit /b 1
    )

    echo Starting Ollama...
    start "" /min "%OLLAMA_EXE%" serve
    timeout /t 2 /nobreak >nul
)

echo Starting Local Screen Translator...
".venv\Scripts\python.exe" app.py

pause