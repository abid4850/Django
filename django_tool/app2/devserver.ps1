# Devserver for Windows PowerShell
# Tries to use uvicorn (ASGI) with --reload; falls back to `manage.py runserver` if uvicorn is not installed.
$ErrorActionPreference = 'Stop'
Write-Host "Starting development server for app2..."

# Check for uvicorn
python -c "import importlib, sys; importlib.import_module('uvicorn')" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "uvicorn found — starting ASGI server with reload..."
    python -m uvicorn app2.asgi:application --reload --host 127.0.0.1 --port 8000
} else {
    Write-Host "uvicorn not found — starting Django runserver (auto-reload)"
    python manage.py runserver
}
