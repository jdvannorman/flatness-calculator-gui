import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calculate_flatness():
    try:
        h = float(height_entry.get())
        l = float(length_entry.get())

        h_unit = height_unit.get()
        l_unit = length_unit.get()

        # Convert mm to inches if necessary
        if h_unit == "mm":
            h /= 25.4
        if l_unit == "mm":
            l /= 25.4

        if l == 0:
            raise ZeroDivisionError("Length cannot be zero.")

        result = 2.467 * ((h / l) ** 2) * 1e5
        result_label.config(
            text=f"Imperial: {result:.2f} I units\nMetric: {result * 0.0254:.2f} I (metric)"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Input Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Flatness Calculator")

# App icon (works after .exe build)
try:
    root.iconbitmap("assets/app_icon.ico")
except:
    pass

# Load logo image
logo_img = Image.open("assets/logo.png")
logo_img = logo_img.resize((120, 120))
logo = ImageTk.PhotoImage(logo_img)

ttk.Label(root, image=logo).grid(row=0, column=0, columnspan=4, pady=10)

# Height input
ttk.Label(root, text="Height:").grid(row=1, column=0, sticky="e", padx=5)
height_entry = ttk.Entry(root)
height_entry.grid(row=1, column=1)

height_unit = ttk.Combobox(root, values=["inches", "mm"], width=7, state="readonly")
height_unit.set("inches")
height_unit.grid(row=1, column=2)
height_entry.insert(0, "0")

# Tooltip
height_entry_tooltip = tk.Label(root, text="Vertical deviation", foreground="gray")
height_entry_tooltip.grid(row=1, column=3, sticky="w")

# Length input
ttk.Label(root, text="Length:").grid(row=2, column=0, sticky="e", padx=5)
length_entry = ttk.Entry(root)
length_entry.grid(row=2, column=1)

length_unit = ttk.Combobox(root, values=["inches", "mm"], width=7, state="readonly")
length_unit.set("inches")
length_unit.grid(row=2, column=2)
length_entry.insert(0, "0")

length_entry_tooltip = tk.Label(root, text="Total length of the object", foreground="gray")
length_entry_tooltip.grid(row=2, column=3, sticky="w")

# Calculate button
ttk.Button(root, text="Calculate", command=calculate_flatness).grid(row=3, column=0, columnspan=4, pady=10)

# Output
result_label = ttk.Label(root, text="Imperial: \nMetric:")
result_label.grid(row=4, column=0, columnspan=4, pady=10)

# Credits
ttk.Label(root, text="Coded by Daniel Van Norman & Anthony Scrivner", font=("Arial", 8)).grid(
    row=5, column=0, columnspan=4, pady=5
)

root.mainloop()
