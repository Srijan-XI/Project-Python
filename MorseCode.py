import tkinter as tk
from tkinter import messagebox

class MorseConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")

        self.morse = ["-----", ".----", "..---", "...--", "....-",
                      ".....", "-....", "--...", "---..", "----."]
        self.num_to_morse = {str(i): self.morse[i] for i in range(10)}
        self.morse_to_num = {v: str(i) for i, v in enumerate(self.morse)}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Number or Morse Code:", font=("Arial", 12)).pack(pady=5)

        self.input_entry = tk.Entry(self.root, font=("Courier", 14), width=30)
        self.input_entry.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Number to Morse", command=self.number_to_morse, width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Morse to Number", command=self.morse_to_number, width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Show Morse Chart", command=self.show_chart, width=15).grid(row=1, column=0, pady=5)
        tk.Button(button_frame, text="Clear", command=self.clear_all, width=15).grid(row=1, column=1, pady=5)

    def number_to_morse(self):
        input_text = self.input_entry.get()
        result = []

        for char in input_text:
            if char.isdigit():
                result.append(self.num_to_morse[char])
            else:
                result.append("[Invalid]")
        self.result_label.config(text="Morse Code: " + ' '.join(result))

    def morse_to_number(self):
        input_text = self.input_entry.get().strip()
        codes = input_text.split()
        result = ""

        for code in codes:
            result += self.morse_to_num.get(code, "?")
        self.result_label.config(text="Number: " + result)

    def show_chart(self):
        chart = "\n".join([f"{i} : {self.num_to_morse[str(i)]}" for i in range(10)])
        messagebox.showinfo("Morse Code Chart", chart)

    def clear_all(self):
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = MorseConverterGUI(root)
    root.geometry("400x300")
    root.mainloop()