import tkinter as tk
from tkinter import ttk

# Conversion functions for each category
conversion_factors = {
    'Length': {
        'Meter': 1.0,
        'Kilometer': 1000.0,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Foot': 0.3048,
        'Inch': 0.0254
    },
    'Weight': {
        'Kilogram': 1.0,
        'Gram': 0.001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    },
    'Temperature': {
        'Celsius': 'C',
        'Fahrenheit': 'F',
        'Kelvin': 'K'
    },
    'Volume': {
        'Litre': 1.0,
        'Millilitre': 0.001,
        'Gallon': 3.78541
    },
    'Speed': {
        'Km/h': 1.0,
        'Mph': 1.60934,
        'Knots': 1.852,
        'Mach': 1234.8
    },
    'Power': {
        'Watt': 1.0,
        'Kilowatt': 1000.0,
        'Horsepower': 745.7
    },
    'Area': {
        'Sq. Meter': 1.0,
        'Sq. Foot': 0.092903,
        'Sq. Kilometer': 1e6,
        'Sq. Centimeter': 0.0001
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return None

def convert_units():
    category = category_cb.get()
    from_unit = from_cb.get()
    to_unit = to_cb.get()
    try:
        value = float(entry.get())
    except ValueError:
        result_label.config(text="Enter a valid number.")
        return

    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        try:
            factor_from = conversion_factors[category][from_unit]
            factor_to = conversion_factors[category][to_unit]
            result = value * (factor_from / factor_to)
        except KeyError:
            result = None

    if result is None:
        result_label.config(text="Conversion error.")
    else:
        result_label.config(text=f"{result:.4f} {to_unit}")

def update_units(event=None):
    category = category_cb.get()
    units = list(conversion_factors[category].keys())
    from_cb['values'] = units
    to_cb['values'] = units
    from_cb.set(units[0])
    to_cb.set(units[1])

# GUI Setup
root = tk.Tk()
root.title("Smart Unit Converter")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="Universal Unit Converter", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Category:").grid(row=0, column=0, padx=10, pady=5)
category_cb = ttk.Combobox(frame, state="readonly", width=20)
category_cb['values'] = list(conversion_factors.keys())
category_cb.grid(row=0, column=1)
category_cb.bind("<<ComboboxSelected>>", update_units)
category_cb.set("Length")  # Default category

tk.Label(frame, text="From Unit:").grid(row=1, column=0, padx=10, pady=5)
from_cb = ttk.Combobox(frame, state="readonly", width=20)
from_cb.grid(row=1, column=1)

tk.Label(frame, text="To Unit:").grid(row=2, column=0, padx=10, pady=5)
to_cb = ttk.Combobox(frame, state="readonly", width=20)
to_cb.grid(row=2, column=1)

tk.Label(frame, text="Value:").grid(row=3, column=0, padx=10, pady=5)
entry = tk.Entry(frame)
entry.grid(row=3, column=1)

tk.Button(root, text="Convert", command=convert_units, width=20, bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

update_units()  # Initialize defaults

root.mainloop()
