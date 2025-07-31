import tkinter as tk
from tkinter import messagebox

def calculate_flatness():
    try:
        H = float(entry_H.get())
        L = float(entry_L.get())
        if L == 0:
            raise ZeroDivisionError
        I = ((3.1415 * H) / (2 * L)) ** 2 * 1e5
        result_label.config(text=f"Flatness I = {I:.2f}")
    except ZeroDivisionError:
        messagebox.showerror("Input Error", "L cannot be zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Flatness Calculator")

tk.Label(root, text="Enter H:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="Enter L:").grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_H = tk.Entry(root)
entry_L = tk.Entry(root)
entry_H.grid(row=0, column=1, pady=5)
entry_L.grid(row=1, column=1, pady=5)

tk.Button(root, text="Calculate", command=calculate_flatness).grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
