from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize translator
translator = Translator()

# Translation dictionary (fallback)
TRANSLATION_DICT = {
    'hello': 'ನಮಸ್ಕಾರ',
    'good morning': 'ಶುಭೋದಯ',
    'good afternoon': 'ಶುಭ ಸಂಜೆ',
    'good evening': 'ಶುಭ ಸಂಜೆ',
    'good night': 'ಶುಭ ರಾತ್ರಿ',
    'thank you': 'ಧನ್ಯವಾದ',
    'thanks': 'ಧನ್ಯವಾದ',
    'please': 'ದಯವಿಟ್ಟು',
    'yes': 'ಹೌದು',
    'no': 'ಇಲ್ಲ',
    'ok': 'ಸರಿ',
    'okay': 'ಸರಿ',
    'how are you': 'ನೀವು ಹೇಗಿದ್ದೀರಿ',
    'i am fine': 'ನಾನು ಸರಿಯಿದೆ',
    'what is your name': 'ನಿಮ್ಮ ಹೆಸರು ಏನು',
    'my name is': 'ನನ್ನ ಹೆಸರು',
    'nice to meet you': 'ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗುತ್ತಲೆ ಸಂತೋಷವಾಗಿದೆ',
    'where are you from': 'ನೀವು ಎಲ್ಲಿ ಇಂದ ಇರುತ್ತೀರಿ',
    'water': 'ನೀರು',
    'food': 'ಆಹಾರ',
    'help': 'ಸಹಾಯ',
    'friend': 'ಗೆಳೆಯ',
    'family': 'ಕುಟುಂಬ',
    'love': 'ಪ್ರೀತಿ',
    'happy': 'ಸಂತೋಷ',
    'sad': 'ದುಃಖ',
    'welcome': 'ಸ್ವಾಗತ',
    'bye': 'ವಿದಾಯ',
    'goodbye': 'ವಿದಾಯ',
    'one': 'ಒಂದು',
    'two': 'ಎರಡು',
    'three': 'ಮೂರು',
    'four': 'ನಾಲ್ಕು',
    'five': 'ಐದು',
    'white': 'ಬಿಳಿ',
    'black': 'ಕಪ್ಪು',
    'red': 'ಕೆಂಪು',
    'blue': 'ನೀಲಿ',
    'green': 'ಹಸಿರು',
    'yellow': 'ಹಳದಿ',
}


@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate():
    """API endpoint for translation"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'message': 'Please enter text to translate',
                'translation': ''
            }), 400
        
        # Try Google Translate API first
        try:
            translation = translator.translate(text, src_language='en', dest_language='kn')
            translated_text = translation['text']
            method = 'Google Translate'
        except Exception as e:
            print(f"Google Translate error: {e}")
            # Fallback to dictionary
            translated_text = translate_with_dictionary(text)
            method = 'Dictionary Fallback'
        
        return jsonify({
            'success': True,
            'translation': translated_text,
            'method': method,
            'message': 'Translation successful!'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}',
            'translation': ''
        }), 500


@app.route('/speak', methods=['POST'])
def speak():
    """API endpoint for text-to-speech (browser handles this)"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        language = data.get('language', 'en')
        
        if not text:
            return jsonify({
                'success': False,
                'message': 'No text to speak'
            }), 400
        
        # Browser will handle speech synthesis
        return jsonify({
            'success': True,
            'message': 'Audio will be played in browser',
            'text': text,
            'language': language
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500


def translate_with_dictionary(text):
    """Fallback dictionary translation"""
    words = text.split()
    translated_words = []
    
    for word in words:
        clean_word = word.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        if clean_word in TRANSLATION_DICT:
            translated_words.append(TRANSLATION_DICT[clean_word])
        else:
            translated_words.append(word)
    
    return ' '.join(translated_words)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'English to Kannada Translator'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
