#!/usr/bin/env python3
"""
Setup script to install dependencies and check requirements
"""

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is 3.6 or higher"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        sys.exit(1)
    print(f"✓ Python {sys.version.split()[0]} detected")

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Error installing packages")
        sys.exit(1)

def run_app():
    """Run the translator application"""
    print("\n🚀 Starting English to Kannada Translator...")
    try:
        subprocess.call([sys.executable, "translator_app.py"])
    except Exception as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

def main():
    print("=" * 50)
    print("  English to Kannada Translator Setup")
    print("=" * 50)
    
    check_python_version()
    install_requirements()
    
    print("\n" + "=" * 50)
    print("✓ Setup complete! Starting application...")
    print("=" * 50)
    
    run_app()

if __name__ == "__main__":
    main()
