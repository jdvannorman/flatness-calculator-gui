import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)
        self.tipwindow = None
    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x, y, _, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        tw = self.tipwindow = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         bg="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
    def hide_tip(self, event=None):
        tw = self.tipwindow; self.tipwindow = None
        if tw: tw.destroy()

def convert_to_inches(value, unit):
    return value / 25.4 if unit == 'mm' else value

def convert_to_mm(value, unit):
    return value * 25.4 if unit == 'inch' else value

def calculate_flatness():
    try:
        H_val = float(entry_H.get())
        L_val = float(entry_L.get())
        H_unit = unit_H.get()
        L_unit = unit_L.get()
        if L_val == 0:
            raise ZeroDivisionError
        H_in = convert_to_inches(H_val, H_unit)
        L_in = convert_to_inches(L_val, L_unit)
        I = 2.467 * ((H_in / L_in) ** 2) * 1e5
        H_mm = convert_to_mm(H_val, H_unit)
        L_mm = convert_to_mm(L_val, L_unit)
        result_label.config(text=(
            f"Flatness I‑Units: {I:.2f}\n\n"
            f"Height = {H_mm:.2f} mm / {H_in:.3f} in\n"
            f"Length = {L_mm:.2f} mm / {L_in:.3f} in"
        ))
    except ZeroDivisionError:
        messagebox.showerror("Input Error", "Length (L) cannot be zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Flatness Calculator")

# Insert logo if exists
logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
if os.path.isfile(logo_path):
    img = Image.open(logo_path)
    img = img.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    logo_label = tk.Label(root, image=photo)
    logo_label.image = photo
    logo_label.grid(row=0, column=0, columnspan=3, pady=(10,5))

# Inputs
tk.Label(root, text="Height (H):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_H = tk.Entry(root); entry_H.grid(row=1, column=1)
unit_H = ttk.Combobox(root, values=['mm', 'inch'], width=5); unit_H.current(0)
unit_H.grid(row=1, column=2, padx=5)

tk.Label(root, text="Length (L):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_L = tk.Entry(root); entry_L.grid(row=2, column=1)
unit_L = ttk.Combobox(root, values=['mm', 'inch'], width=5); unit_L.current(1)
unit_L.grid(row=2, column=2, padx=5)

calc_btn = tk.Button(root, text="Calculate", command=calculate_flatness)
calc_btn.grid(row=3, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", justify='left')
result_label.grid(row=4, column=0, columnspan=3, pady=10)

credits = "© 2025 Daniel Van Norman & Anthony Scrivner"
credits_label = tk.Label(root, text=credits, font=("Arial",8), fg="gray")
credits_label.grid(row=5, column=0, columnspan=3, pady=(0,10))

# Tooltips
ToolTip(entry_H, "Enter height value; units selectable.")
ToolTip(unit_H, "Unit for height: mm or inches.")
ToolTip(entry_L, "Enter length value; units selectable.")
ToolTip(unit_L, "Unit for length: mm or inches.")
ToolTip(calc_btn, "Calculate using I = 2.467*(H/L)^2*10^5 with conversions.")

root.mainloop()
