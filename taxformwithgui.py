import tkinter as tk

def calculate_tax():
    try:
        tax = float(income_entry.get()) * float(tax_rate_entry.get()) / 100
        result_label.config(text=f"Tax Owed: ${tax:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Tax Calculator")

for text in ["Income:", "Tax Rate (%):"]:
    tk.Label(root, text=text).pack()
    entry = tk.Entry(root)
    entry.pack()
    if text == "Income:":
        income_entry = entry
    else:
        tax_rate_entry = entry

tk.Button(root, text="Calculate", command=calculate_tax).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
