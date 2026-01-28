# Quick Start Guide

## 🚀 Getting Started with English to Kannada Translator

### Option 1: Windows Users (Easiest) ⭐

1. **Double-click `run.bat`** in the project folder
2. It will automatically install dependencies
3. The application will launch!

---

### Option 2: Command Line Setup

**For Windows:**
```cmd
cd c:\Users\student\english-to-kannada-tansalator
pip install -r requirements.txt
python translator_app.py
```

**For macOS/Linux:**
```bash
cd english-to-kannada-tansalator
pip install -r requirements.txt
python3 translator_app.py
```

---

### Option 3: Using Setup Script

**Windows:**
```cmd
python setup.py
```

**macOS/Linux:**
```bash
python3 setup.py
```

---

## ⚙️ System Setup (If Needed)

If you encounter a Python not found error:

1. **Install Python from** https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation
   - Download Python 3.8 or higher

2. **After installing Python**, restart your terminal/command prompt

3. **Then run:**
   ```cmd
   pip install -r requirements.txt
   python translator_app.py
   ```

---

## 📦 What Gets Installed

The following packages are automatically installed:
- **pyttsx3** - Text-to-speech engine
- **googletrans** - Translation API
- **requests** - HTTP library

Total size: ~50-100 MB

---

## 🎯 Using the Application

1. **Type English text** in the left box
2. **Click Translate** to convert to Kannada
3. **Click Speak English/Kannada** to hear pronunciation
4. **Click Copy** to copy the translation
5. **Click Clear** to reset

---

## 🐛 Troubleshooting

### "Python is not recognized"
- Make sure Python is installed and added to PATH
- Restart your computer after installing Python
- Use `py -m pip install -r requirements.txt` instead

### "ModuleNotFoundError"
- Run `pip install -r requirements.txt` again
- Try: `pip install --upgrade -r requirements.txt`

### Text-to-speech not working
- Check your system volume
- Make sure speakers/headphones are connected
- Reinstall pyttsx3: `pip install --upgrade pyttsx3`

### Translation not working
- Check your internet connection
- Application will use dictionary fallback if API fails
- Try restarting the application

---

## 💡 Tips

- You can resize the application window
- Double-click words in Kannada text box to select them
- Use Ctrl+A to select all, Ctrl+C to copy
- The dictionary has 40+ pre-translated words
- Speech rate can be adjusted in translator_app.py (line 35)

---

**Questions? Check the README.md file for more details!**
