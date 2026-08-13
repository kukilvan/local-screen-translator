@echo off
cd /d C:\local_screen_translator\local_screen_translator
netstat -ano | findstr ":11434" | findstr "LISTENING" >nul
if errorlevel 1 (
    powershell -NoProfile -WindowStyle Hidden -Command "Start-Process -FilePath 'C:\Users\erudi\AppData\Local\Programs\Ollama\ollama.exe' -ArgumentList 'serve' -WindowStyle Hidden"
    timeout /t 2 /nobreak >nul
)
start "" ".venv\Scripts\pythonw.exe" app.py
