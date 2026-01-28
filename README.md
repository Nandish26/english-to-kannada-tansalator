# English to Kannada Translator with Text-to-Speech

A powerful Python desktop application that translates English text to Kannada with integrated text-to-speech functionality.

## Features

✨ **Key Features:**
- 🌐 Real-time English to Kannada translation using Google Translate API
- 🔊 Text-to-speech for both English and Kannada (pyttsx3)
- 📋 Copy translated text to clipboard
- 🎨 Modern GUI built with tkinter
- ⚡ Fast and lightweight
- 💾 Built-in dictionary fallback (100+ translations)
- 🔧 Easy to use and configure

## Translation Methods

The application uses multiple translation approaches:

1. **Google Translate API** - Accurate, real-time translations
2. **Fallback Dictionary** - Built-in dictionary for common words and phrases
3. **Hybrid Approach** - Automatically falls back to dictionary if API is unavailable

## Text-to-Speech

- Uses pyttsx3 for offline text-to-speech
- Natural pronunciation in both English and Kannada
- Adjustable speech rate and volume
- Stop/pause speech functionality

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Quick Start (Windows)

1. **Download/Clone the project**
   ```bash
   cd english-to-kannada-translator
   ```

2. **Run the application (Easiest)**
   ```bash
   run.bat
   ```
   This will automatically install dependencies and launch the app.

### Manual Installation

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python translator_app.py
   ```

### Or use the setup script
```bash
python setup.py
```

## Usage Steps

1. **Enter Text**: Type or paste English text in the left text box
2. **Translate**: Click the "🔄 Translate" button to convert to Kannada
3. **Listen**: 
   - Click "🔊 Speak English" to hear English pronunciation
   - Click "🔊 Speak Kannada" to hear Kannada pronunciation
4. **Copy**: Click "📋 Copy" to copy the translated text
5. **Clear**: Click "Clear" to reset the English text
6. **Stop**: Click "Stop Speech" to stop audio playback

## File Structure

```
english-to-kannada-translator/
├── translator_app.py      # Main Python application with GUI
├── setup.py              # Setup and installation script
├── run.bat               # Windows batch file to run the app
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── index.html            # (Optional) Web version
├── style.css             # (Optional) Web version styles
└── script.js             # (Optional) Web version JavaScript
```

## System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.6 or higher
- **RAM**: 512 MB minimum
- **Storage**: 100 MB for dependencies
- **Network**: Internet connection (for Google Translate API)

## Dependencies

```
pyttsx3==2.90          # Text-to-speech
googletrans==4.0.0     # Translation API
requests==2.31.0       # HTTP requests
```

## Translation Dictionary

The application includes a built-in dictionary with 40+ common words and phrases:

**Sample translations:**
- hello → ನಮಸ್ಕಾರ
- thank you → ಧನ್ಯವಾದ
- water → ನೀರು
- friend → ಗೆಳೆಯ
- happy → ಸಂತೋಷ
- ... and many more!

## Troubleshooting

### Issue: "Module not found" error
**Solution:** Run `pip install -r requirements.txt` to install dependencies

### Issue: Text-to-speech not working
**Solution:** 
- Check system volume is not muted
- Try adjusting speech rate in code (line 35: `self.engine.setProperty('rate', 150)`)
- Reinstall pyttsx3: `pip install --upgrade pyttsx3`

### Issue: Translation returning English text
**Solution:**
- Check internet connection
- The dictionary fallback will be used if API fails
- Try restarting the application

### Issue: Poor audio quality
**Solution:**
- Different OS/systems have different voice qualities
- Try adjusting speech rate in the code
- Install additional voice packs on your system

## License

This project is open source and available for personal and educational use.

## Author

English to Kannada Translator with Python
Created: January 2026

## Support

For issues, suggestions, or contributions:
- Report bugs
- Suggest new features
- Improve the dictionary
- Enhance the UI/UX

## API Information

**Google Translate API (googletrans)**
- Free to use via googletrans library
- No API key required
- Language pair: English ↔ Kannada
- Rate limits may apply

---

**Happy Translating! 🎉**

## Keyboard Shortcuts

- **Ctrl+A**: Select all text
- **Ctrl+C**: Copy text
- **Ctrl+V**: Paste text
