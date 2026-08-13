@echo off

powershell -NoProfile -WindowStyle Hidden -Command "Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -ne $PID -and $_.Name -match '^python(w)?\.exe$' -and $_.CommandLine -and ($_.CommandLine -like '*local_screen_translator*app.py*' -or $_.CommandLine -like '*local_screen_translator*align_worker.py*') } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }"

taskkill /F /T /IM ollama.exe >nul 2>&1
taskkill /F /T /IM "ollama app.exe" >nul 2>&1
taskkill /F /T /IM llama-server.exe >nul 2>&1

exit /b 0