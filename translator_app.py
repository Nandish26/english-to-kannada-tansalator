import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import pyttsx3
from googletrans import Translator
import requests
import json

class KannadaTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Kannada Translator with Text-to-Speech")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Initialize translator and text-to-speech
        self.translator = Translator()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)
        
        # Translation dictionary (fallback)
        self.translation_dict = {
            'hello': 'ನಮಸ್ಕಾರ',
            'good morning': 'ಶುಭೋದಯ',
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
        
        # Flag for stopping speech
        self.is_speaking = False
        
        self.setup_ui()
        self.show_info_message("Welcome! Enter English text and click Translate")
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title = ttk.Label(header_frame, text="🌐 English to Kannada Translator", 
                         font=("Arial", 18, "bold"))
        title.pack()
        
        subtitle = ttk.Label(header_frame, text="Translate English text to Kannada with Text-to-Speech",
                            font=("Arial", 10))
        subtitle.pack()
        
        # Content frame
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - English
        left_frame = ttk.LabelFrame(content_frame, text="English (EN)", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.english_text = scrolledtext.ScrolledText(left_frame, height=15, width=40,
                                                       font=("Arial", 11), wrap=tk.WORD)
        self.english_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.english_text.insert(1.0, "Enter English text here...")
        self.english_text.bind("<FocusIn>", self.on_english_focus_in)
        self.english_text.bind("<FocusOut>", self.on_english_focus_out)
        
        english_btn_frame = ttk.Frame(left_frame)
        english_btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(english_btn_frame, text="🔊 Speak English", 
                  command=self.speak_english).pack(side=tk.LEFT, padx=2)
        ttk.Button(english_btn_frame, text="Clear", 
                  command=self.clear_english).pack(side=tk.LEFT, padx=2)
        
        # Right side - Kannada
        right_frame = ttk.LabelFrame(content_frame, text="ಕನ್ನಡ (Kannada - KN)", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.kannada_text = scrolledtext.ScrolledText(right_frame, height=15, width=40,
                                                       font=("Noto Sans Kannada", 11), wrap=tk.WORD)
        self.kannada_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.kannada_text.config(state=tk.DISABLED)
        
        kannada_btn_frame = ttk.Frame(right_frame)
        kannada_btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(kannada_btn_frame, text="🔊 Speak Kannada", 
                  command=self.speak_kannada).pack(side=tk.LEFT, padx=2)
        ttk.Button(kannada_btn_frame, text="📋 Copy", 
                  command=self.copy_kannada).pack(side=tk.LEFT, padx=2)
        
        # Button frame - Translate
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)
        
        self.translate_btn = ttk.Button(button_frame, text="🔄 Translate",
                                        command=self.translate_text)
        self.translate_btn.pack(side=tk.LEFT, expand=True, padx=5)
        
        ttk.Button(button_frame, text="Stop Speech", 
                  command=self.stop_speech).pack(side=tk.LEFT, padx=5)
        
        # Message frame
        self.message_frame = ttk.Frame(main_frame)
        self.message_frame.pack(fill=tk.X, pady=10)
        
        self.message_var = tk.StringVar()
        self.message_label = ttk.Label(self.message_frame, textvariable=self.message_var,
                                       font=("Arial", 9))
        self.message_label.pack()
        
        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="ℹ️ How to Use", padding=10)
        info_frame.pack(fill=tk.X, pady=10)
        
        info_text = """1. Type or paste English text in the left box
2. Click "Translate" to convert to Kannada
3. Use speaker buttons to hear pronunciation
4. Click "Copy" to copy the translated text"""
        
        ttk.Label(info_frame, text=info_text, font=("Arial", 9), 
                 justify=tk.LEFT).pack(anchor=tk.W)
    
    def on_english_focus_in(self, event):
        """Clear placeholder text on focus"""
        if self.english_text.get(1.0, tk.END).strip() == "Enter English text here...":
            self.english_text.delete(1.0, tk.END)
    
    def on_english_focus_out(self, event):
        """Restore placeholder text if empty"""
        if not self.english_text.get(1.0, tk.END).strip():
            self.english_text.insert(1.0, "Enter English text here...")
    
    def translate_text(self):
        """Translate English text to Kannada"""
        text = self.english_text.get(1.0, tk.END).strip()
        
        if not text or text == "Enter English text here...":
            self.show_error_message("Please enter English text")
            return
        
        # Disable button during translation
        self.translate_btn.config(state=tk.DISABLED)
        self.show_info_message("Translating...")
        
        # Run translation in a separate thread to avoid freezing UI
        thread = threading.Thread(target=self._perform_translation, args=(text,))
        thread.start()
    
    def _perform_translation(self, text):
        """Perform the actual translation"""
        try:
            # Try using Google Translate API first
            translation = self.translator.translate(text, src_language='en', dest_language='kn')
            translated_text = translation['text']
            
            # Update the UI from the main thread
            self.root.after(0, self._update_kannada_text, translated_text, "Translation successful!")
        except Exception as e:
            print(f"Translation error: {e}")
            # Fallback to dictionary
            translated_text = self._translate_using_dictionary(text)
            self.root.after(0, self._update_kannada_text, translated_text, 
                          "Translation completed using dictionary")
    
    def _translate_using_dictionary(self, text):
        """Translate using fallback dictionary"""
        words = text.split()
        translated_words = []
        
        for word in words:
            clean_word = word.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
            if clean_word in self.translation_dict:
                translated_words.append(self.translation_dict[clean_word])
            else:
                translated_words.append(word)
        
        return ' '.join(translated_words)
    
    def _update_kannada_text(self, text, message):
        """Update Kannada text box"""
        self.kannada_text.config(state=tk.NORMAL)
        self.kannada_text.delete(1.0, tk.END)
        self.kannada_text.insert(1.0, text)
        self.kannada_text.config(state=tk.DISABLED)
        
        self.translate_btn.config(state=tk.NORMAL)
        self.show_success_message(message)
    
    def speak_english(self):
        """Speak English text"""
        text = self.english_text.get(1.0, tk.END).strip()
        
        if not text or text == "Enter English text here...":
            self.show_error_message("Please enter English text")
            return
        
        self.is_speaking = True
        thread = threading.Thread(target=self._speak_text, args=(text, 'en'))
        thread.start()
    
    def speak_kannada(self):
        """Speak Kannada text"""
        text = self.kannada_text.get(1.0, tk.END).strip()
        
        if not text:
            self.show_error_message("Please translate first")
            return
        
        self.is_speaking = True
        thread = threading.Thread(target=self._speak_text, args=(text, 'kn'))
        thread.start()
    
    def _speak_text(self, text, language):
        """Speak text using pyttsx3"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.root.after(0, lambda: self.show_error_message(f"Text-to-speech error: {str(e)}"))
        finally:
            self.is_speaking = False
    
    def stop_speech(self):
        """Stop current speech"""
        try:
            self.engine.stop()
            self.is_speaking = False
            self.show_info_message("Speech stopped")
        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")
    
    def clear_english(self):
        """Clear English text"""
        self.english_text.delete(1.0, tk.END)
        self.english_text.insert(1.0, "Enter English text here...")
        self.english_text.focus()
    
    def copy_kannada(self):
        """Copy Kannada text to clipboard"""
        text = self.kannada_text.get(1.0, tk.END).strip()
        
        if not text:
            self.show_error_message("Nothing to copy")
            return
        
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.show_success_message("Copied to clipboard!")
        except Exception as e:
            self.show_error_message(f"Copy error: {str(e)}")
    
    def show_success_message(self, message):
        """Show success message"""
        self.message_var.set(f"✓ {message}")
        self.message_label.config(foreground="green")
        self.root.after(3000, lambda: self.message_var.set(""))
    
    def show_error_message(self, message):
        """Show error message"""
        self.message_var.set(f"✗ {message}")
        self.message_label.config(foreground="red")
        self.root.after(3000, lambda: self.message_var.set(""))
    
    def show_info_message(self, message):
        """Show info message"""
        self.message_var.set(f"ℹ {message}")
        self.message_label.config(foreground="blue")
        self.root.after(3000, lambda: self.message_var.set(""))


def main():
    root = tk.Tk()
    app = KannadaTranslatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
