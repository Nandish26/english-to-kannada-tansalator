// English to Kannada Translator - Flask Application
// Frontend JavaScript

// DOM Elements
const englishText = document.getElementById('englishText');
const kannadaText = document.getElementById('kannadaText');
const translateBtn = document.getElementById('translateBtn');
const speakEnglishBtn = document.getElementById('speakEnglishBtn');
const speakKannadaBtn = document.getElementById('speakKannadaBtn');
const clearEnglishBtn = document.getElementById('clearEnglishBtn');
const copyKannadaBtn = document.getElementById('copyKannadaBtn');
const messageDiv = document.getElementById('message');
const historySection = document.getElementById('historySection');
const historyList = document.getElementById('historyList');

// State
let translationHistory = JSON.parse(localStorage.getItem('translationHistory')) || [];
let isSpeaking = false;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    loadTranslationHistory();
    showMessage('Welcome! Enter English text and click Translate', 'info');
});

// Setup Event Listeners
function setupEventListeners() {
    translateBtn.addEventListener('click', translateText);
    speakEnglishBtn.addEventListener('click', speakEnglish);
    speakKannadaBtn.addEventListener('click', speakKannada);
    clearEnglishBtn.addEventListener('click', clearEnglish);
    copyKannadaBtn.addEventListener('click', copyToClipboard);
    
    // Allow Enter key to translate
    englishText.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            translateText();
        }
    });
}

// Translate Text
async function translateText() {
    const text = englishText.value.trim();
    
    if (!text) {
        showMessage('Please enter English text', 'error');
        return;
    }
    
    // Disable button and show loading
    translateBtn.disabled = true;
    showMessage('Translating...', 'info');
    
    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (data.success) {
            kannadaText.value = data.translation;
            
            // Add to history
            addToHistory(text, data.translation);
            
            showMessage(`✓ ${data.message} (${data.method})`, 'success');
        } else {
            showMessage(data.message, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showMessage('Translation failed. Please try again.', 'error');
    } finally {
        translateBtn.disabled = false;
    }
}

// Speak English
function speakEnglish() {
    const text = englishText.value.trim();
    
    if (!text) {
        showMessage('Please enter English text', 'error');
        return;
    }
    
    speak(text, 'en-US');
}

// Speak Kannada
function speakKannada() {
    const text = kannadaText.value.trim();
    
    if (!text) {
        showMessage('Please translate first', 'error');
        return;
    }
    
    speak(text, 'kn-IN');
}

// Speech Synthesis
function speak(text, language) {
    // Stop any current speech
    window.speechSynthesis.cancel();
    
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = language;
    utterance.rate = 1;
    utterance.pitch = 1;
    utterance.volume = 1;
    
    utterance.onstart = function() {
        isSpeaking = true;
        showMessage('🔊 Speaking...', 'info');
    };
    
    utterance.onend = function() {
        isSpeaking = false;
        showMessage('✓ Finished speaking', 'success');
    };
    
    utterance.onerror = function(event) {
        isSpeaking = false;
        showMessage(`Speech error: ${event.error}`, 'error');
    };
    
    window.speechSynthesis.speak(utterance);
}

// Clear English Text
function clearEnglish() {
    englishText.value = '';
    englishText.focus();
    showMessage('Text cleared', 'info');
}

// Copy to Clipboard
function copyToClipboard() {
    const text = kannadaText.value.trim();
    
    if (!text) {
        showMessage('Nothing to copy', 'error');
        return;
    }
    
    navigator.clipboard.writeText(text).then(function() {
        showMessage('✓ Copied to clipboard!', 'success');
    }).catch(function(err) {
        showMessage('Failed to copy', 'error');
        console.error('Error:', err);
    });
}

// Show Message
function showMessage(message, type = 'info') {
    messageDiv.textContent = message;
    messageDiv.className = `message ${type}`;
    
    // Auto-clear after 3 seconds
    setTimeout(function() {
        messageDiv.textContent = '';
        messageDiv.className = 'message empty';
    }, 3000);
}

// Translation History
function addToHistory(english, kannada) {
    const entry = {
        english: english,
        kannada: kannada,
        timestamp: new Date().toISOString()
    };
    
    // Add to beginning of array
    translationHistory.unshift(entry);
    
    // Keep only last 20 items
    if (translationHistory.length > 20) {
        translationHistory.pop();
    }
    
    // Save to localStorage
    localStorage.setItem('translationHistory', JSON.stringify(translationHistory));
    
    // Update UI
    loadTranslationHistory();
}

function loadTranslationHistory() {
    if (translationHistory.length === 0) {
        historySection.style.display = 'none';
        return;
    }
    
    historySection.style.display = 'block';
    historyList.innerHTML = '';
    
    translationHistory.forEach((item, index) => {
        const historyItem = document.createElement('div');
        historyItem.className = 'history-item';
        
        const textDiv = document.createElement('div');
        textDiv.className = 'history-item-text';
        textDiv.innerHTML = `
            <div class="history-item-en">${escapeHtml(item.english)}</div>
            <div class="history-item-kn">${escapeHtml(item.kannada)}</div>
        `;
        
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'history-item-delete';
        deleteBtn.innerHTML = '✕';
        deleteBtn.title = 'Delete this item';
        deleteBtn.onclick = function(e) {
            e.stopPropagation();
            translationHistory.splice(index, 1);
            localStorage.setItem('translationHistory', JSON.stringify(translationHistory));
            loadTranslationHistory();
        };
        
        historyItem.appendChild(textDiv);
        historyItem.appendChild(deleteBtn);
        
        // Click to restore
        historyItem.addEventListener('click', function() {
            englishText.value = item.english;
            kannadaText.value = item.kannada;
            englishText.focus();
            showMessage('✓ Restored from history', 'info');
        });
        
        historyList.appendChild(historyItem);
    });
}

// Utility Functions
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Prevent closing while speaking
window.addEventListener('beforeunload', function(e) {
    if (isSpeaking) {
        e.preventDefault();
        e.returnValue = '';
    }
});

// Handle visibility change to pause speech
document.addEventListener('visibilitychange', function() {
    if (document.hidden && isSpeaking) {
        window.speechSynthesis.pause();
    } else if (!document.hidden && isSpeaking) {
        window.speechSynthesis.resume();
    }
});
