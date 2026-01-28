@echo off
REM English to Kannada Translator Launcher
REM This script runs the translator application

echo.
echo ========================================
echo English to Kannada Translator Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher from https://www.python.org
    pause
    exit /b 1
)

REM Install requirements if needed
echo Checking dependencies...
python -m pip install -q -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Starting application...
python translator_app.py

pause
