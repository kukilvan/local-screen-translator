# Run this PowerShell as Administrator.
$ErrorActionPreference = "Stop"

Write-Host "Installing Windows English OCR capability..." -ForegroundColor Cyan
Add-WindowsCapability -Online -Name "Language.OCR~~~en-US~0.0.1.0"
Write-Host "Done. A reboot is usually not required." -ForegroundColor Green
