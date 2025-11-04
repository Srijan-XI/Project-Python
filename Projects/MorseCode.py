"""
Advanced Morse Code Converter
==============================
A comprehensive Morse code converter with support for:
- Full alphabet (A-Z), numbers (0-9), and special characters
- Text to Morse and Morse to Text conversion
- Audio playback of Morse code
- Copy to clipboard functionality
- Interactive Morse code chart
- Modern and intuitive GUI

Author: Enhanced Version
Date: November 2025
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import winsound
import threading
from typing import Dict

class MorseConverterGUI:
    # Complete Morse code dictionary
    MORSE_CODE: Dict[str, str] = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    
    # Reverse dictionary for decoding
    REVERSE_MORSE: Dict[str, str] = {v: k for k, v in MORSE_CODE.items()}
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔊 Advanced Morse Code Converter")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#2c3e50')
        
        # Configure grid weights for responsiveness
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_rowconfigure(4, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = tk.Label(main_frame, text="🔊 Morse Code Converter", 
                               font=("Arial", 20, "bold"), bg='#2c3e50', fg='#ecf0f1')
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Input Section
        input_frame = tk.LabelFrame(main_frame, text="📝 Input Text", 
                                    font=("Arial", 11, "bold"),
                                    bg='#34495e', fg='#ecf0f1', padx=10, pady=10)
        input_frame.grid(row=1, column=0, sticky='ew', pady=5)
        input_frame.grid_columnconfigure(0, weight=1)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, height=6, 
                                                    font=("Courier New", 11),
                                                    wrap=tk.WORD, bg='#ecf0f1')
        self.input_text.grid(row=0, column=0, sticky='ew')
        
        # Control Buttons
        control_frame = tk.Frame(main_frame, bg='#2c3e50')
        control_frame.grid(row=2, column=0, pady=10)
        
        btn_style = {
            'font': ("Arial", 10, "bold"),
            'width': 18,
            'height': 2,
            'relief': tk.RAISED,
            'bd': 3
        }
        
        tk.Button(control_frame, text="🔽 Text to Morse", 
                 command=self.text_to_morse, bg='#3498db', fg='white',
                 activebackground='#2980b9', **btn_style).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(control_frame, text="🔼 Morse to Text", 
                 command=self.morse_to_text, bg='#2ecc71', fg='white',
                 activebackground='#27ae60', **btn_style).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(control_frame, text="🔊 Play Audio", 
                 command=self.play_morse_audio, bg='#e74c3c', fg='white',
                 activebackground='#c0392b', **btn_style).grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(control_frame, text="📋 Copy Result", 
                 command=self.copy_to_clipboard, bg='#9b59b6', fg='white',
                 activebackground='#8e44ad', **btn_style).grid(row=1, column=1, padx=5, pady=5)
        
        # Output Section
        output_frame = tk.LabelFrame(main_frame, text="📤 Output", 
                                     font=("Arial", 11, "bold"),
                                     bg='#34495e', fg='#ecf0f1', padx=10, pady=10)
        output_frame.grid(row=3, column=0, sticky='ew', pady=5)
        output_frame.grid_columnconfigure(0, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=6, 
                                                     font=("Courier New", 11),
                                                     wrap=tk.WORD, bg='#ecf0f1',
                                                     state=tk.DISABLED)
        self.output_text.grid(row=0, column=0, sticky='ew')
        
        # Bottom Buttons
        bottom_frame = tk.Frame(main_frame, bg='#2c3e50')
        bottom_frame.grid(row=4, column=0, pady=10)
        
        btn_style2 = {
            'font': ("Arial", 10),
            'width': 15,
            'relief': tk.RAISED,
            'bd': 2
        }
        
        tk.Button(bottom_frame, text="📊 Show Chart", 
                 command=self.show_chart, bg='#f39c12', fg='white',
                 activebackground='#e67e22', **btn_style2).grid(row=0, column=0, padx=5)
        
        tk.Button(bottom_frame, text="ℹ️ Help", 
                 command=self.show_help, bg='#16a085', fg='white',
                 activebackground='#138d75', **btn_style2).grid(row=0, column=1, padx=5)
        
        tk.Button(bottom_frame, text="🗑️ Clear All", 
                 command=self.clear_all, bg='#95a5a6', fg='white',
                 activebackground='#7f8c8d', **btn_style2).grid(row=0, column=2, padx=5)

    
    def text_to_morse(self):
        """Convert regular text to Morse code."""
        input_text = self.input_text.get("1.0", tk.END).strip().upper()
        
        if not input_text:
            messagebox.showwarning("Empty Input", "Please enter some text to convert!")
            return
        
        morse_result = []
        for char in input_text:
            if char in self.MORSE_CODE:
                morse_result.append(self.MORSE_CODE[char])
            elif char == '\n':
                morse_result.append('\n')
            else:
                morse_result.append('?')
        
        result = ' '.join(morse_result)
        self.display_output(result)
        self.update_status(f"✅ Converted {len(input_text)} characters to Morse code")
    
    def morse_to_text(self):
        """Convert Morse code to regular text."""
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Empty Input", "Please enter Morse code to convert!")
            return
        
        # Split by newlines to handle multiple lines
        lines = input_text.split('\n')
        decoded_lines = []
        
        for line in lines:
            # Split by spaces to get individual Morse codes
            codes = line.split()
            decoded_chars = []
            
            for code in codes:
                if code in self.REVERSE_MORSE:
                    decoded_chars.append(self.REVERSE_MORSE[code])
                elif code == '':
                    continue
                else:
                    decoded_chars.append('?')
            
            decoded_lines.append(''.join(decoded_chars))
        
        result = '\n'.join(decoded_lines)
        self.display_output(result)
        self.update_status(f"✅ Decoded Morse code to text")
    
    def play_morse_audio(self):
        """Play Morse code as audio beeps."""
        morse_text = self.output_text.get("1.0", tk.END).strip()
        
        if not morse_text:
            messagebox.showwarning("No Output", "Please convert text to Morse first!")
            return
        
        # Run audio in separate thread to avoid blocking UI
        thread = threading.Thread(target=self._play_morse_thread, args=(morse_text,))
        thread.daemon = True
        thread.start()
        self.update_status("🔊 Playing Morse code audio...")
    
    def _play_morse_thread(self, morse_text):
        """Play Morse code audio in a separate thread."""
        DOT_DURATION = 100  # milliseconds
        DASH_DURATION = 300  # milliseconds
        FREQUENCY = 800  # Hz
        
        for char in morse_text:
            if char == '.':
                winsound.Beep(FREQUENCY, DOT_DURATION)
            elif char == '-':
                winsound.Beep(FREQUENCY, DASH_DURATION)
            elif char == ' ':
                winsound.Beep(37, 100)  # Short pause between letters
            elif char == '/':
                winsound.Beep(37, 300)  # Longer pause between words
        
        self.update_status("✅ Audio playback completed")
    
    def copy_to_clipboard(self):
        """Copy output to clipboard."""
        output = self.output_text.get("1.0", tk.END).strip()
        
        if not output:
            messagebox.showwarning("No Output", "Nothing to copy!")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(output)
        self.root.update()
        self.update_status("✅ Copied to clipboard!")
        messagebox.showinfo("Success", "Output copied to clipboard!")
    
    def show_chart(self):
        """Display a comprehensive Morse code chart."""
        chart_window = tk.Toplevel(self.root)
        chart_window.title("📊 Morse Code Chart")
        chart_window.geometry("600x500")
        chart_window.configure(bg='#2c3e50')
        
        # Title
        tk.Label(chart_window, text="International Morse Code Chart", 
                font=("Arial", 16, "bold"), bg='#2c3e50', fg='#ecf0f1').pack(pady=10)
        
        # Create scrolled text for chart
        chart_text = scrolledtext.ScrolledText(chart_window, font=("Courier New", 10),
                                               bg='#ecf0f1', wrap=tk.WORD)
        chart_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Build chart content
        chart_content = "═" * 50 + "\n"
        chart_content += "LETTERS:\n"
        chart_content += "═" * 50 + "\n"
        
        for i, (letter, code) in enumerate(sorted(self.MORSE_CODE.items())[:26], 1):
            chart_content += f"{letter}: {code:8} "
            if i % 3 == 0:
                chart_content += "\n"
        
        chart_content += "\n" + "═" * 50 + "\n"
        chart_content += "NUMBERS:\n"
        chart_content += "═" * 50 + "\n"
        
        for num in '0123456789':
            chart_content += f"{num}: {self.MORSE_CODE[num]:8} "
        
        chart_content += "\n\n" + "═" * 50 + "\n"
        chart_content += "SPECIAL CHARACTERS:\n"
        chart_content += "═" * 50 + "\n"
        
        special = [k for k in self.MORSE_CODE.keys() if not k.isalnum() and k != ' ']
        for i, char in enumerate(special, 1):
            chart_content += f"{char}: {self.MORSE_CODE[char]:8} "
            if i % 3 == 0:
                chart_content += "\n"
        
        chart_content += "\n\n" + "═" * 50 + "\n"
        chart_content += "TIMING:\n"
        chart_content += "═" * 50 + "\n"
        chart_content += "• Dot (.): 1 unit\n"
        chart_content += "• Dash (-): 3 units\n"
        chart_content += "• Gap between parts: 1 unit\n"
        chart_content += "• Gap between letters: 3 units\n"
        chart_content += "• Gap between words: 7 units\n"
        
        chart_text.insert("1.0", chart_content)
        chart_text.config(state=tk.DISABLED)
    
    def show_help(self):
        """Display help information."""
        help_text = """
🔊 Advanced Morse Code Converter - Help

HOW TO USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Text to Morse:
   1. Enter your text in the input box
   2. Click "Text to Morse" button
   3. Result appears in output box

🔤 Morse to Text:
   1. Enter Morse code (use spaces between letters)
   2. Click "Morse to Text" button
   3. Decoded text appears in output

🔊 Audio Playback:
   • Convert text to Morse first
   • Click "Play Audio" to hear the code
   • Dot (.) = short beep
   • Dash (-) = long beep

📋 Copy to Clipboard:
   • Click to copy output
   • Paste anywhere you need

MORSE CODE FORMAT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Use spaces between letters
• Use "/" for word separation
• Example: "... --- ..." = SOS

SUPPORTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ All letters (A-Z)
✓ All numbers (0-9)
✓ Special characters (. , ? ! etc.)
✓ Multi-line text

Created with ❤️ for Morse code enthusiasts!
        """
        messagebox.showinfo("Help", help_text)
    
    def clear_all(self):
        """Clear all input and output fields."""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.update_status("🗑️ All fields cleared")
    
    def display_output(self, text):
        """Display text in the output area."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.config(state=tk.DISABLED)
    
    def update_status(self, message):
        """Update status (could be extended to a status bar)."""
        self.root.title(f"🔊 Morse Code Converter - {message}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseConverterGUI(root)
    root.mainloop()