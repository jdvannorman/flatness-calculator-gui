import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Pillow is required for image support

class ToolTip:
    # Simple tooltip implementation
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def convert_to_inches(value, unit):
    if unit == 'mm':
        return value / 25.4
    return value

def convert_to_mm(value, unit):
    if unit == 'inch':
        return value * 25.4
    return value

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

        result_text = (
            f"Flatness I = {I:.2f} I-Units\n\n"
            f"Height: {H_mm:.2f} mm / {H_in:.3f} in\n"
            f"Length: {L_mm:.2f} mm / {L_in:.3f} in"
        )
        result_label.config(text=result_text)
    except ZeroDivisionError:
        messagebox.showerror("Input Error", "Length (L) cannot be zero.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Flatness Calculator with Units & Help")

# --- Add Logo at the top ---
try:
    logo_image = Image.open("Logo.png")  # Load the image
    logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10)
except Exception as e:
    print("Error loading logo:", e)

# Height input
tk.Label(root, text="Enter Height (H):").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_H = tk.Entry(root)
entry_H.grid(row=0, column=1, pady=5, sticky='w')

unit_H = ttk.Combobox(root, values=['mm', 'inch'], width=5)
unit_H.current(0)
unit_H.grid(row=0, column=2, padx=5, pady=5)

# Length input
tk.Label(root, text="Enter Length (L):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_L = tk.Entry(root)
entry_L.grid(row=1, column=1, pady=5, sticky='w')

unit_L = ttk.Combobox(root, values=['mm', 'inch'], width=5)
unit_L.current(1)
unit_L.grid(row=1, column=2, padx=5, pady=5)

# Calculate button
calc_btn = tk.Button(root, text="Calculate", command=calculate_flatness)
calc_btn.grid(row=2, column=0, columnspan=3, pady=10)

# Result label
result_label = tk.Label(root, text="", justify='left')
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# --- Add credits at the bottom ---
credit_label = tk.Label(root, text="Coded by: Daniel Van Norman & Anthony Scrivner", font=("Arial", 9, "italic"))
credit_label.grid(row=4, column=0, columnspan=4, pady=(5, 10))

# Tooltips
ToolTip(entry_H, "Enter height value.\nUnits selectable on the right.")
ToolTip(unit_H, "Select unit for height: mm or inches.")
ToolTip(entry_L, "Enter length value.\nUnits selectable on the right.")
ToolTip(unit_L, "Select unit for length: mm or inches.")
ToolTip(calc_btn, "Click to calculate flatness using:\nI = 2.467 * (H/L)^2 * 10^5\nwith units conversion.")

root.mainloop()
