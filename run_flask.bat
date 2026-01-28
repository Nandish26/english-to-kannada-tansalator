@echo off
REM Flask English to Kannada Translator Launcher
echo.
echo ========================================
echo Flask English to Kannada Translator
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

REM Install requirements
echo Installing dependencies...
python -m pip install -q -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Starting Flask application...
echo Application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
