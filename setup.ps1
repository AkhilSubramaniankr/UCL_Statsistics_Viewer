# UCL Elite Analytics Platform - Setup Script

Write-Host "==========================================" -ForegroundColor Green
Write-Host "UCL Elite Analytics Platform Setup" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

# Check Python
Write-Host "`n[1/5] Checking Python..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK - $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "ERROR - Python not found" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher" -ForegroundColor Red
    exit 1
}

# Create venv
Write-Host "`n[2/5] Creating virtual environment..." -ForegroundColor Yellow
if (!(Test-Path "venv")) {
    python -m venv venv
    Write-Host "OK - Created" -ForegroundColor Green
} else {
    Write-Host "OK - Already exists" -ForegroundColor Green
}

# Activate venv
Write-Host "`n[3/5] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "OK - Activated" -ForegroundColor Green

# Install requirements
Write-Host "`n[4/5] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK - Installed" -ForegroundColor Green
} else {
    Write-Host "ERROR - Installation failed" -ForegroundColor Red
    exit 1
}

# Setup .env
Write-Host "`n[5/5] Setting up environment file..." -ForegroundColor Yellow
if (!(Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "OK - Created .env file" -ForegroundColor Green
    Write-Host "IMPORTANT - Edit .env and add your OPENAI_API_KEY" -ForegroundColor Yellow
} else {
    Write-Host "OK - .env already exists" -ForegroundColor Green
}

Write-Host "`n==========================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Edit .env and add OPENAI_API_KEY" -ForegroundColor White
Write-Host "2. Run: streamlit run app.py" -ForegroundColor White
Write-Host "`nDocumentation:" -ForegroundColor Yellow
Write-Host "See INDEX.md for complete guide" -ForegroundColor White
