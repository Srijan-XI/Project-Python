import tkinter as tk
from tkinter import messagebox

def click_button(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(value))

def clear_display():
    entry_display.delete(0, tk.END)

def backspace():
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current[:-1])

def calculate_result():
    try:
        expression = entry_display.get().replace('%', '/100')
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is undefined.")
        entry_display.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Error", "Invalid input.")
        entry_display.delete(0, tk.END)

window = tk.Tk()
window.title("GUI Calculator")
window.geometry("350x480")
window.resizable(False, False)

entry_display = tk.Entry(window, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

buttons = [
    ('C', '%', '⌫', '/'),
    ('7', '8', '9', '*'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('00', '0', '.', '='),
]

for r, row in enumerate(buttons, start=1):
    for c, btn_text in enumerate(row):
        if btn_text == 'C':
            action = clear_display
        elif btn_text == '⌫':
            action = backspace
        elif btn_text == '=':
            action = calculate_result
        else:
            action = lambda val=btn_text: click_button(val)

        tk.Button(
            window,
            text=btn_text,
            font=("Arial", 14),
            width=6,
            height=2,
            relief=tk.RAISED,
            command=action
        ).grid(row=r, column=c, padx=5, pady=5)

window.mainloop()
