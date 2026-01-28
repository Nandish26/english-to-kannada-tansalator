# Flask English to Kannada Translator

A modern web application built with Flask that translates English text to Kannada with integrated text-to-speech functionality.

## Overview

This is a **Flask-based web application** that provides:
- Real-time English to Kannada translation
- Web browser-based text-to-speech
- Translation history with localStorage
- RESTful API endpoints
- Responsive modern UI with HTML/CSS

## Features

🌐 **Translation**
- Google Translate API integration
- Dictionary fallback (40+ common words)
- Batch translation support

🔊 **Text-to-Speech**
- Browser-based Web Speech API
- Support for English (US) and Kannada (IN)
- Adjustable speech rate and pitch

💾 **History Management**
- Automatic translation history saving
- LocalStorage persistence
- One-click restore functionality

🎨 **Modern UI**
- Responsive design
- Gradient styling
- Smooth animations
- Mobile-friendly

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Modern web browser

### Quick Start (Windows)

```bash
# 1. Navigate to project folder
cd english-to-kannada-translator

# 2. Run the launcher
run_flask.bat
```

The application will start at `http://localhost:5000`

### Manual Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

Then open your browser to `http://localhost:5000`

## Project Structure

```
english-to-kannada-translator/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── run_flask.bat                   # Windows launcher
│
├── templates/
│   └── index.html                  # Main HTML template
│
└── static/
    ├── css/
    │   └── style.css              # Styling
    └── js/
        └── script.js              # Frontend JavaScript
```

## How to Use

### Basic Workflow

1. **Enter English Text**
   - Type or paste English text in the left box

2. **Click Translate**
   - The Flask backend processes the request
   - Translation appears in the right box

3. **Hear the Pronunciation**
   - Click "🔊 Speak English" or "🔊 Speak Kannada"
   - Browser plays audio using Web Speech API

4. **Copy Translation**
   - Click "📋 Copy" to copy to clipboard
   - Click on history items to restore them

## API Endpoints

### POST /translate
Translate English text to Kannada

**Request:**
```json
{
  "text": "hello"
}
```

**Response:**
```json
{
  "success": true,
  "translation": "ನಮಸ್ಕಾರ",
  "method": "Google Translate",
  "message": "Translation successful!"
}
```

### POST /speak
Endpoint for speech (handled by browser)

**Request:**
```json
{
  "text": "hello",
  "language": "en"
}
```

### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "English to Kannada Translator"
}
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3 | Web framework |
| googletrans | 4.0.0 | Translation API |
| requests | 2.31.0 | HTTP library |
| Werkzeug | 2.3.7 | WSGI utility |

## Configuration

### Flask Settings (app.py)

```python
# Debug mode (set to False in production)
app.run(debug=True, host='0.0.0.0', port=5000)

# Speech rate (in script.js)
utterance.rate = 1;  # Range: 0.5 - 2

# Keep history for 20 items (script.js)
if (translationHistory.length > 20) { translationHistory.pop(); }
```

## Translation Methods

### 1. Google Translate API
- Primary method
- Real-time translation
- Requires internet connection
- Accurate for longer texts

### 2. Dictionary Fallback
- Used if API fails
- 40+ pre-translated words
- Works offline
- Fast response time

### 3. Hybrid Approach
- Tries API first
- Falls back to dictionary
- Always returns a result

## Features in Detail

### Translation History
- Saves up to 20 recent translations
- Uses browser's localStorage
- Click items to restore
- Delete button for each item
- Persists across sessions

### Text-to-Speech
- Uses Web Speech API (no external service)
- Supports multiple languages
- Adjustable speech parameters
- Stops on tab change
- Error handling included

### Responsive Design
- Mobile (< 480px)
- Tablet (480px - 768px)
- Desktop (> 768px)
- Print-friendly styles

## Troubleshooting

### "Flask not found"
```bash
pip install Flask==2.3.3
```

### "ModuleNotFoundError: No module named 'googletrans'"
```bash
pip install -r requirements.txt
```

### Translation API Error
- Check internet connection
- Application automatically uses dictionary fallback
- Try again after a few seconds

### Text-to-Speech Not Working
- Check browser's microphone/speaker settings
- Ensure volume is not muted
- Try a different browser (Chrome works best)
- Check if Kannada language pack is installed

### Port Already in Use
```bash
# Change port in app.py
app.run(port=5001)  # Use different port
```

## Performance Tips

1. **Caching Translations**
   - History is automatically cached in localStorage
   - API results are cached by browser

2. **Optimize Images**
   - Minimal external resources
   - Efficient CSS with gradients

3. **Lazy Loading**
   - Speech synthesis loads on demand
   - API calls only when needed

## Security Considerations

- CSRF protection via Flask
- Input sanitization in JavaScript
- No sensitive data stored locally
- Safe JSON parsing

## Browser Compatibility

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome | ✅ Full | Best text-to-speech support |
| Firefox | ✅ Full | Good support |
| Safari | ✅ Full | iOS/macOS compatible |
| Edge | ✅ Full | Chromium-based |
| Opera | ✅ Full | Chromium-based |
| IE 11 | ❌ No | Not supported |

## Development

### Running in Development Mode
```bash
python app.py
```

### Running in Production
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Testing the API
```bash
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"text":"hello"}'
```

## Customization

### Add More Translations
Edit the `TRANSLATION_DICT` in `app.py`:
```python
TRANSLATION_DICT = {
    'your_word': 'ನೀವು ಅನುವಾದ',
    # ... more translations
}
```

### Change Color Scheme
Edit `:root` variables in `static/css/style.css`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    /* ... */
}
```

### Modify Speech Settings
In `static/js/script.js`:
```javascript
utterance.rate = 1;    // Speech speed
utterance.pitch = 1;   // Voice pitch
utterance.volume = 1;  // Volume level
```

## License

Open source and available for personal and educational use.

## Author

Flask English to Kannada Translator
Created: January 2026

## Support

- Check README.md for general information
- Check QUICKSTART.md for setup help
- Report issues or suggest improvements

## Future Enhancements

- [ ] Add voice input (speech recognition)
- [ ] Support more languages
- [ ] User authentication
- [ ] Cloud translation service integration
- [ ] PDF/document translation
- [ ] API rate limiting
- [ ] Translation quality scores
- [ ] Multi-language UI

---

**Happy Translating! 🎉**
