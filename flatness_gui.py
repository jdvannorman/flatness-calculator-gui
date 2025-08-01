import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calculate_flatness():
    try:
        h = float(entry_height.get())
        l = float(entry_length.get())

        if unit_var.get() == "mm":
            h_inches = h / 25.4
            l_inches = l / 25.4
        else:
            h_inches = h
            l_inches = l

        I = 2.467 * ((h_inches / l_inches) ** 2) * 1e5

        I_mm = I * 25.4
        result_var.set(f"Imperial: {I:.2f} in⁻¹\nMetric: {I_mm:.2f} mm⁻¹")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Flatness Calculator")
root.geometry("400x450")
root.resizable(False, False)

# Load and display logo
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource (works for dev and for PyInstaller) """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logo_img = Image.open(resource_path("assets/logo.png"))
logo_img = logo_img.resize((100, 100))
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(pady=10)

unit_var = tk.StringVar(value="inches")

frame = ttk.Frame(root, padding=10)
frame.pack()

ttk.Label(frame, text="Height:").grid(row=0, column=0, sticky="e")
entry_height = ttk.Entry(frame)
entry_height.grid(row=0, column=1)
entry_height.insert(0, "0")

ttk.Label(frame, text="Length:").grid(row=1, column=0, sticky="e")
entry_length = ttk.Entry(frame)
entry_length.grid(row=1, column=1)
entry_length.insert(0, "1")

ttk.Label(frame, text="Units:").grid(row=2, column=0, sticky="e")
unit_menu = ttk.OptionMenu(frame, unit_var, "inches", "inches", "mm")
unit_menu.grid(row=2, column=1, sticky="ew")

ttk.Button(root, text="Calculate", command=calculate_flatness).pack(pady=10)

result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, font=("Segoe UI", 12)).pack()

ttk.Label(root, text="Coded by Daniel Van Norman & Anthony Scrivner", font=("Segoe UI", 9)).pack(pady=20)

# Tooltips
def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.withdraw()
    tooltip.overrideredirect(True)
    label = tk.Label(tooltip, text=text, background="lightyellow", relief="solid", borderwidth=1, font=("Segoe UI", 8))
    label.pack()

    def enter(event):
        tooltip.deiconify()
        x = event.x_root + 10
        y = event.y_root + 10
        tooltip.geometry(f"+{x}+{y}")

    def leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

create_tooltip(entry_height, "Enter height in selected unit")
create_tooltip(entry_length, "Enter length in selected unit")
create_tooltip(unit_menu, "Select input units")

root.mainloop()
