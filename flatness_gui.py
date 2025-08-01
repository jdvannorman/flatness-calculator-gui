import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calculate_flatness():
    try:
        height = float(height_entry.get())
        length = float(length_entry.get())

        if units_var.get() == "Metric (mm & mm)":
            height_in = height / 25.4
            length_in = length / 25.4
        else:
            height_in = height
            length_in = length

        i_units = 2.467 * (height_in / length_in) ** 2 * 1e5
        result_label.config(text=f"Flatness: {i_units:.2f} I-Units")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input.\n{e}")

app = tk.Tk()
app.title("Flatness Calculator")

# Load logo
logo = Image.open("assets/logo.png")
logo = logo.resize((100, 100))
logo_tk = ImageTk.PhotoImage(logo)
tk.Label(app, image=logo_tk).pack()

# Title and credits
tk.Label(app, text="Flatness Calculator", font=("Helvetica", 16)).pack(pady=5)
tk.Label(app, text="Coded by Daniel Van Norman & Anthony Scrivner", font=("Arial", 8)).pack()

# Input frame
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

units_var = tk.StringVar(value="Imperial (mm & inches)")
unit_menu = ttk.Combobox(frame, textvariable=units_var, values=[
    "Imperial (mm & inches)",
    "Metric (mm & mm)"
], state="readonly", width=30)
unit_menu.grid(row=0, column=0, columnspan=2, pady=5)
unit_menu_tooltip = "Choose units:\n- Imperial: Height in mm, Length in inches\n- Metric: Height & Length in mm"
unit_menu.bind("<Enter>", lambda e: app.title(unit_menu_tooltip))

tk.Label(frame, text="Height:").grid(row=1, column=0, sticky="e")
height_entry = tk.Entry(frame)
height_entry.grid(row=1, column=1)

tk.Label(frame, text="Length:").grid(row=2, column=0, sticky="e")
length_entry = tk.Entry(frame)
length_entry.grid(row=2, column=1)

tk.Button(app, text="Calculate", command=calculate_flatness).pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
