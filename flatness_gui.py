import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

def calculate_flatness():
    try:
        h = float(height_entry.get())
        l = float(length_entry.get())

        # Convert to inches internally
        h_in = h if height_unit.get() == "in" else h / 25.4
        l_in = l if length_unit.get() == "in" else l / 25.4

        if l_in == 0:
            raise ZeroDivisionError("Length cannot be zero.")

        i_units = 2.467 * (h_in / l_in) ** 2 * 1e5

        # Convert back to mm for display
        h_mm = h if height_unit.get() == "mm" else h * 25.4
        l_mm = l if length_unit.get() == "mm" else l * 25.4

        result_label.config(text=f"I-Units: {i_units:.2f}")
        details_label.config(
            text=f"Height: {h:.2f} {height_unit.get()} ({h_mm:.2f} mm), "
                 f"Length: {l:.2f} {length_unit.get()} ({l_mm:.2f} mm)"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Flatness Calculator")

# Load logo
logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
if os.path.exists(logo_path):
    logo_img = Image.open(logo_path).resize((100, 100))
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

# Height input
tk.Label(root, text="Height:").grid(row=1, column=0, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)
height_unit = ttk.Combobox(root, values=["mm", "in"], width=5)
height_unit.set("mm")
height_unit.grid(row=1, column=2)

# Length input
tk.Label(root, text="Length:").grid(row=2, column=0, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=2, column=1)
length_unit = ttk.Combobox(root, values=["in", "mm"], width=5)
length_unit.set("in")
length_unit.grid(row=2, column=2)

# Tooltip
tooltip = tk.Label(
    root,
    text="Formula: I = 2.467 × (H/L)² × 10⁵ (H & L in inches)",
    fg="gray"
)
tooltip.grid(row=3, column=0, columnspan=3, pady=(5, 0))

# Calculate button
tk.Button(root, text="Calculate", command=calculate_flatness).grid(row=4, column=0, columnspan=3, pady=10)

# Output labels
result_label = tk.Label(root, text="I-Units: ")
result_label.grid(row=5, column=0, columnspan=3)

details_label = tk.Label(root, text="", fg="gray")
details_label.grid(row=6, column=0, columnspan=3)

# Credits
tk.Label(root, text="© Coded by Daniel Van Norman & Anthony Scrivner", font=("Arial", 8), fg="gray").grid(row=7, column=0, columnspan=3, pady=(10, 5))

root.mainloop()
