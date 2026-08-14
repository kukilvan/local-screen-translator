@echo off
setlocal
cd /d "%~dp0"

set "LST_PROJECT_DIR=%~dp0"

powershell -NoProfile -WindowStyle Hidden -Command "$project=$env:LST_PROJECT_DIR.TrimEnd('\'); Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -ne $PID -and $_.Name -match '^python(w)?\.exe$' -and $_.ExecutablePath -and $_.ExecutablePath.StartsWith($project, [System.StringComparison]::OrdinalIgnoreCase) -and $_.CommandLine -and ($_.CommandLine -like '*app.py*' -or $_.CommandLine -like '*align_worker.py*') } | ForEach-Object { & taskkill.exe /F /T /PID $_.ProcessId 2>$null | Out-Null }"

taskkill /F /T /IM ollama.exe >nul 2>&1
taskkill /F /T /IM "ollama app.exe" >nul 2>&1
taskkill /F /T /IM llama-server.exe >nul 2>&1

exit /b 0