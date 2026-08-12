$ErrorActionPreference = "Stop"

Write-Host "Searching NVIDIA GPUs..." -ForegroundColor Cyan

$rows = nvidia-smi --query-gpu=name,uuid --format=csv,noheader
$target = $rows | Where-Object { $_ -match "RTX 3070 Ti" } | Select-Object -First 1

if (-not $target) {
    Write-Host ""
    Write-Host "RTX 3070 Ti was not found. nvidia-smi reported:" -ForegroundColor Red
    $rows | ForEach-Object { Write-Host "  $_" }
    exit 1
}

$parts = $target -split ","
$gpuName = $parts[0].Trim()
$gpuUuid = $parts[1].Trim()

Write-Host "Target GPU: $gpuName" -ForegroundColor Green
Write-Host "UUID:       $gpuUuid" -ForegroundColor Green

# Persist for Ollama Windows app. UUID is safer than numeric GPU index.
[Environment]::SetEnvironmentVariable("CUDA_VISIBLE_DEVICES", $gpuUuid, "User")

# Privacy: local models/API only.
[Environment]::SetEnvironmentVariable("OLLAMA_NO_CLOUD", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "127.0.0.1:11434", "User")

# This utility sends one request at a time. Keep scheduling/memory simple.
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_MAX_LOADED_MODELS", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "2048", "User")

Write-Host ""
Write-Host "Done." -ForegroundColor Green
Write-Host "IMPORTANT: fully Quit Ollama from the Windows tray, then start it again."
Write-Host "After restart run: ollama pull qwen3:4b-instruct"
Write-Host "Then verify with: ollama ps"
