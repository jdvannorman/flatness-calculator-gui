import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calculate_flatness():
    try:
        H_value = float(height_entry.get())
        L_value = float(length_entry.get())

        # Convert height if it's in mm
        if height_unit.get() == 'mm':
            H_value /= 25.4  # mm to inches

        # Convert length if it's in mm
        if length_unit.get() == 'mm':
            L_value /= 25.4  # mm to inches

        if L_value == 0:
            raise ValueError("Length cannot be zero.")

        I_units = 2.467 * ((H_value / L_value) ** 2) * 1e5

        result_var.set(f"Flatness: {I_units:,.2f} I-Units\n"
                       f"(H = {H_value:.4f} in, L = {L_value:.4f} in)")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

app = tk.Tk()
app.title("Flatness Calculator")

# Logo
try:
    logo_img = Image.open("assets/logo.png")
    logo_img = logo_img.resize((80, 80))
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = ttk.Label(app, image=logo)
    logo_label.grid(row=0, column=0, columnspan=4, pady=(10, 0))
except Exception:
    pass

# Input Fields
ttk.Label(app, text="Height (H):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
height_entry = ttk.Entry(app)
height_entry.grid(row=1, column=1)

height_unit = ttk.Combobox(app, values=["mm", "in"], width=5, state="readonly")
height_unit.current(0)
height_unit.grid(row=1, column=2)

ttk.Label(app, text="Length (L):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
length_entry = ttk.Entry(app)
length_entry.grid(row=2, column=1)

length_unit = ttk.Combobox(app, values=["in", "mm"], width=5, state="readonly")
length_unit.current(0)
length_unit.grid(row=2, column=2)

# Tooltip info (simple labels for now)
ttk.Label(app, text="* Height and Length must be > 0").grid(row=3, column=0, columnspan=4)

# Calculate button
ttk.Button(app, text="Calculate Flatness", command=calculate_flatness).grid(row=4, column=0, columnspan=4, pady=10)

# Result
result_var = tk.StringVar()
ttk.Label(app, textvariable=result_var, font=("Segoe UI", 10, "bold")).grid(row=5, column=0, columnspan=4, pady=5)

# Credits
ttk.Label(app, text="Coded by Daniel Van Norman & Anthony Scrivner", font=("Segoe UI", 8)).grid(row=6, column=0, columnspan=4, pady=10)

app.mainloop()
