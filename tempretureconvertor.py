import tkinter as tk

def convert(temp, to_celsius):
    try:
        val = float(temp.get())
        result = (val - 32) * 5 / 9 if to_celsius else (val * 9 / 5) + 32
        (celsius_entry if to_celsius else fahrenheit_entry).delete(0, tk.END)
        (celsius_entry if to_celsius else fahrenheit_entry).insert(0, f"{result:.2f}")
    except ValueError:
        (celsius_entry if to_celsius else fahrenheit_entry).delete(0, tk.END)
        (celsius_entry if to_celsius else fahrenheit_entry).insert(0, "Invalid")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Fahrenheit").grid(row=0, column=0)
tk.Label(root, text="Celsius").grid(row=0, column=1)

fahrenheit_entry, celsius_entry = tk.Entry(root), tk.Entry(root)
fahrenheit_entry.grid(row=1, column=0)
celsius_entry.grid(row=1, column=1)

fahrenheit_entry.insert(0, "32.0")
celsius_entry.insert(0, "0.0")

tk.Button(root, text=">>>>", command=lambda: convert(fahrenheit_entry, True)).grid(row=2, column=0)
tk.Button(root, text="<<<<", command=lambda: convert(celsius_entry, False)).grid(row=2, column=1)

root.mainloop()

