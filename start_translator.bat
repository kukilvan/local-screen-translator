@echo off
cd /d C:\local_screen_translator\local_screen_translator
netstat -ano | findstr ":11434" | findstr "LISTENING" >nul
if errorlevel 1 (
    echo Starting Ollama...
    start "" /min "C:\Users\erudi\AppData\Local\Programs\Ollama\ollama.exe" serve
    timeout /t 2 /nobreak >nul
)
echo Starting Local Screen Translator...
".venv\Scripts\python.exe" app.py
pause
