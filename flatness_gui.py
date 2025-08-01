import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def convert_to_mm(value, unit):
    return value * 25.4 if unit == "inches" else value

def convert_to_inches(value, unit):
    return value / 25.4 if unit == "mm" else value

def calculate_flatness():
    try:
        height = float(height_entry.get())
        height_unit = height_unit_var.get()
        length = float(length_entry.get())
        length_unit = length_unit_var.get()

        height_mm = convert_to_mm(height, height_unit)
        length_in = convert_to_inches(length, length_unit)

        if length_in == 0:
            raise ValueError("Length cannot be zero")

        flatness = height_mm / length_in
        result_var.set(f"Flatness: {flatness:.3f} mm/inch")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Main GUI
app = tk.Tk()
app.title("Flatness Calculator")

# Load and display logo
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and for PyInstaller) """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logo_img = Image.open(resource_path("assets/logo.png"))
logo_img = logo_img.resize((150, 100))
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(image=logo_photo)
logo_label.pack(pady=10)

unit_var = tk.StringVar(value="inches")

frame = ttk.Frame(root, padding=10)
frame.pack()

# Height input
ttk.Label(frame, text="Height:").grid(row=0, column=0, sticky="e")
height_entry = ttk.Entry(frame, width=10)
height_entry.grid(row=0, column=1)
height_unit_var = tk.StringVar(value="mm")
ttk.Combobox(frame, textvariable=height_unit_var, values=["mm", "inches"], width=7).grid(row=0, column=2)

# Length input
ttk.Label(frame, text="Length:").grid(row=1, column=0, sticky="e")
length_entry = ttk.Entry(frame, width=10)
length_entry.grid(row=1, column=1)
length_unit_var = tk.StringVar(value="inches")
ttk.Combobox(frame, textvariable=length_unit_var, values=["mm", "inches"], width=7).grid(row=1, column=2)

# Calculate button and result
ttk.Button(frame, text="Calculate Flatness", command=calculate_flatness).grid(row=2, column=0, columnspan=3, pady=10)
result_var = tk.StringVar()
ttk.Label(frame, textvariable=result_var, font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=3)

app.mainloop()
