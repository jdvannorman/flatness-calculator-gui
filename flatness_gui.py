import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

def convert_units(h_val, h_unit, l_val, l_unit):
    h_in = h_val / 25.4 if h_unit == "mm" else h_val
    l_in = l_val / 25.4 if l_unit == "mm" else l_val
    return h_in, l_in

def calculate_flatness():
    try:
        h = float(height_entry.get())
        l = float(length_entry.get())
        h_unit = height_unit.get()
        l_unit = length_unit.get()

        h_in, l_in = convert_units(h, h_unit, l, l_unit)

        if l_in == 0:
            raise ZeroDivisionError

        i_units = 2.467 * (h_in / l_in) ** 2 * 1e5
        result_label.config(text=f"I-Units: {i_units:.2f}")

        # Optional: show conversion results
        h_mm = h if h_unit == "mm" else h * 25.4
        l_mm = l if l_unit == "mm" else l * 25.4
        details_label.config(
            text=f"Height: {h_mm:.2f} mm | Length: {l_mm:.2f} mm"
        )
    except ZeroDivisionError:
        messagebox.showerror("Error", "Length cannot be zero.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Flatness Calculator")

# Load logo
logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path).resize((100, 100))
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=4, pady=10)

# Height
tk.Label(root, text="Height:").grid(row=1, column=0, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)
height_unit = ttk.Combobox(root, values=["mm", "in"], width=5)
height_unit.set("mm")
height_unit.grid(row=1, column=2)

# Length
tk.Label(root, text="Length:").grid(row=2, column=0, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1)
length_unit = ttk.Combobox(root, values=["mm", "in"], width=5)
length_unit.set("in")
length_unit.grid(row=2, column=2)

# Tooltip
tk.Label(root, text="Units can be switched as needed").grid(row=3, column=0, columnspan=3)

# Calculate
tk.Button(root, text="Calculate", command=calculate_flatness).grid(row=4, column=0, columnspan=3, pady=10)

# Output
result_label = tk.Label(root, text="I-Units: ")
result_label.grid(row=5, column=0, columnspan=3)

details_label = tk.Label(root, text="", fg="gray")
details_label.grid(row=6, column=0, columnspan=3)

# Credits
tk.Label(root, text="© 2025 Daniel Van Norman & Anthony Scrivner", font=("Arial", 8), fg="gray").grid(row=7, column=0, columnspan=4, pady=5)

root.mainloop()
