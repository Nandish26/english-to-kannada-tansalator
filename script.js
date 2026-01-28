// DOM Elements
const englishText = document.getElementById('englishText');
const kannadaText = document.getElementById('kannadaText');
const translateBtn = document.getElementById('translateBtn');
const speakEnglishBtn = document.getElementById('speakEnglish');
const speakKannadaBtn = document.getElementById('speakKannada');
const clearEnglishBtn = document.getElementById('clearEnglish');
const copyKannadaBtn = document.getElementById('copyKannada');
const messageDiv = document.getElementById('message');

// Translation dictionary (Basic Kannada translations)
const translationDictionary = {
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
    'i am from': 'ನಾನು ಅಲ್ಲಿ ಇಂದ ಬಂದಿದೆ',
    'what time is it': 'ಇದು ಎಷ್ಟು ಸಮಯ',
    'can you help me': 'ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡಬಹುದೇ',
    'i love you': 'ನಾನು ನಿಮ್ಮನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ',
    'sorry': 'ಕ್ಷಮೆ',
    'excuse me': 'ಕ್ಷಮೆ',
    'water': 'ನೀರು',
    'food': 'ಆಹಾರ',
    'help': 'ಸಹಾಯ',
    'friend': 'ಗೆಳೆಯ',
    'family': 'ಕುಟುಂಬ',
    'love': 'ಪ್ರೀತಿ',
    'happy': 'ಸಂತೋಷ',
    'sad': 'ದುಃಖ',
    'angry': 'ಕೋಪ',
    'welcome': 'ಸ್ವಾಗತ',
    'bye': 'ವಿದಾಯ',
    'goodbye': 'ವಿದಾಯ',
    'see you': 'ನಿಮ್ಮನ್ನು ಮುಂದೆ ಭೇಟಿಯಾಗೋಣ',
    'one': 'ಒಂದು',
    'two': 'ಎರಡು',
    'three': 'ಮೂರು',
    'four': 'ನಾಲ್ಕು',
    'five': 'ಐದು',
    'six': 'ಆರು',
    'seven': 'ಏಳು',
    'eight': 'ಎಂಟು',
    'nine': 'ಒಂಬತ್ತು',
    'ten': 'ಹತ್ತು',
    'white': 'ಬಿಳಿ',
    'black': 'ಕಪ್ಪು',
    'red': 'ಕೆಂಪು',
    'blue': 'ನೀಲಿ',
    'green': 'ಹಸಿರು',
    'yellow': 'ಹಳದಿ',
    'school': 'ಶಾಲೆ',
    'college': 'ಕಾಲೇಜ್',
    'book': 'ಪುಸ್ತಕ',
    'pen': 'ಪೆನ್ನು',
    'apple': 'ಹೆಚ್ಚಳ',
    'banana': 'ಬಾಳೆಹಣ್ಣು',
    'mango': 'ಮಾವಿನೆ'
};

// Show message
function showMessage(text, type = 'info') {
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    setTimeout(() => {
        messageDiv.textContent = '';
        messageDiv.className = 'message';
    }, 3000);
}

// Speak English text
function speakEnglish() {
    const text = englishText.value.trim();
    if (!text) {
        showMessage('Please enter some English text', 'error');
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 1;
    utterance.pitch = 1;
    speechSynthesis.speak(utterance);
}

// Speak Kannada text
function speakKannada() {
    const text = kannadaText.value.trim();
    if (!text) {
        showMessage('Please translate first', 'error');
        return;
    }

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'kn-IN';
    utterance.rate = 0.8;
    utterance.pitch = 1;
    speechSynthesis.speak(utterance);
}

// Translate English to Kannada
async function translate() {
    const englishInput = englishText.value.trim();

    if (!englishInput) {
        showMessage('Please enter some text to translate', 'error');
        return;
    }

    translateBtn.disabled = true;
    showMessage('Translating...', 'info');

    try {
        // Try using translation API
        const translatedText = await translateText(englishInput);
        kannadaText.value = translatedText;
        showMessage('Translation successful!', 'success');
    } catch (error) {
        console.error('Translation error:', error);
        showMessage('Translation completed using dictionary', 'info');
    } finally {
        translateBtn.disabled = false;
    }
}

// Translate using API or dictionary
async function translateText(text) {
    try {
        // Try using MyMemory Translation API (free, no key required)
        const response = await fetch(
            `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|kn`
        );
        const data = await response.json();

        if (data.responseStatus === 200) {
            return data.responseData.translatedText;
        } else {
            throw new Error('API response error');
        }
    } catch (error) {
        // Fallback to dictionary-based translation
        console.log('Using dictionary fallback');
        return translateUsingDictionary(text);
    }
}

// Dictionary-based translation (fallback)
function translateUsingDictionary(text) {
    let translatedText = text;
    const lowerText = text.toLowerCase();

    // Split by words and translate
    const words = text.split(/\s+/);
    const translatedWords = words.map(word => {
        const cleanWord = word.toLowerCase().replace(/[.,!?;:]/g, '');
        return translationDictionary[cleanWord] || word;
    });

    return translatedWords.join(' ');
}

// Copy to clipboard
function copyToClipboard() {
    const text = kannadaText.value.trim();
    if (!text) {
        showMessage('Nothing to copy', 'error');
        return;
    }

    navigator.clipboard.writeText(text).then(() => {
        showMessage('Copied to clipboard!', 'success');
    }).catch(err => {
        showMessage('Failed to copy', 'error');
    });
}

// Clear English text
function clearEnglish() {
    englishText.value = '';
    englishText.focus();
}

// Event listeners
translateBtn.addEventListener('click', translate);
speakEnglishBtn.addEventListener('click', speakEnglish);
speakKannadaBtn.addEventListener('click', speakKannada);
clearEnglishBtn.addEventListener('click', clearEnglish);
copyKannadaBtn.addEventListener('click', copyToClipboard);

// Allow Enter key to translate
englishText.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        translate();
    }
});

// Auto-translate on input (optional - uncomment to enable)
// englishText.addEventListener('input', () => {
//     if (englishText.value.trim()) {
//         translate();
//     }
// });

// Show initial message
window.addEventListener('load', () => {
    showMessage('Welcome! Enter English text and click Translate', 'info');
});
