import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from PIL import Image, ImageTk

# Unit converter
def convert_to_inches(value, unit):
    if unit == "inches":
        return value
    elif unit == "mm":
        return value / 25.4
    elif unit == "feet":
        return value * 12
    else:
        raise ValueError("Unsupported unit")

def calculate_flatness():
    coil = coil_entry.get().strip()
    if not coil:
        messagebox.showerror("Input Error", "Please enter Coil #.")
        return None

    try:
        h = float(height_entry.get())
        h_unit = height_unit.get()
        l = float(length_entry.get())
        l_unit = length_unit.get()

        h_in = convert_to_inches(h, h_unit)
        l_in = convert_to_inches(l, l_unit)

        if l_in == 0:
            raise ZeroDivisionError("Length cannot be zero.")

        flatness = 2.467 * ((h_in / l_in) ** 2) * 1e5
        flatness_label.config(text=f"Flatness I = {flatness:.2f}")
        return coil, l, l_unit, h, h_unit, flatness
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def export_csv():
    result = calculate_flatness()
    if result:
        coil, l, l_unit, h, h_unit, flatness = result
        default_filename = f"flatness_coil{coil}.csv"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile=default_filename
        )
        if file_path:
            # Append mode so you can keep adding results
            with open(file_path, "a", newline="") as f:
                writer = csv.writer(f)
                # If file is new, write header first
                if f.tell() == 0:
                    writer.writerow(["Coil #", "Length", "Length Unit", "Height", "Height Unit", "Flatness (I)"])
                writer.writerow([coil, l, l_unit, h, h_unit, f"{flatness:.2f}"])
            messagebox.showinfo("Export Successful", f"Data saved to {file_path}")


app = tk.Tk()
app.title("Flatness Calculator")
app.geometry("400x500")
app.resizable(False, False)

# Icon
try:
    app.iconbitmap("assets/app_icon.ico")
except:
    pass

# Logo
try:
    logo_img = Image.open("assets/logo.png").resize((200, 100))
    logo_photo = ImageTk.PhotoImage(logo_img)
    tk.Label(app, image=logo_photo).pack(pady=10)
except:
    pass

# Coil #
tk.Label(app, text="Coil #:").pack()
coil_entry = tk.Entry(app)
coil_entry.pack(pady=5)

# Length
tk.Label(app, text="Length:").pack()
length_frame = tk.Frame(app)
length_entry = tk.Entry(length_frame)
length_entry.pack(side="left")
length_unit = ttk.Combobox(length_frame, values=["inches", "mm", "feet"])
length_unit.set("inches")
length_unit.pack(side="left")
length_frame.pack(pady=5)

# Height
tk.Label(app, text="Height:").pack()
height_frame = tk.Frame(app)
height_entry = tk.Entry(height_frame)
height_entry.pack(side="left")
height_unit = ttk.Combobox(height_frame, values=["mm", "inches", "feet"])
height_unit.set("mm")
height_unit.pack(side="left")
height_frame.pack(pady=5)

# Buttons
tk.Button(app, text="Calculate", command=calculate_flatness).pack(pady=10)
tk.Button(app, text="Export CSV", command=export_csv).pack()

# Result Label
flatness_label = tk.Label(app, text="", font=("Helvetica", 12, "bold"))
flatness_label.pack(pady=10)

# Credits
tk.Label(app, text="Coded by Daniel Van Norman & Anthony Scrivner.", font=("Arial", 9)).pack(side="bottom", pady=10)

app.mainloop()
