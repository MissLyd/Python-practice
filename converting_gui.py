import tkinter as tk
from tkinter import ttk

# 1- Normal conversion function
def conversion(inp,factor,add,unit):
    result = inp*factor + add
    return f"{result:.2f} {unit}"

# 2- Reversed conversion (reversed units)
def reverse_conversion(inp,factor,add,unit):
    result = (inp - add)*factor
    return f"{result:.2f} {unit}"

def perform_conversion():
    try:
        # Input from interface
        inp = float(input_entry.get())
    except ValueError:
        # If error, print error message
        result_label.config(text="Invalid input")
        return

    # Selecting option from conversion options dictionary
    selected_conversion = conversion_options.get()

    conversions={
    "Celsius-Fahrenheit":(inp,9/5,32,"F"),
    "Cups-Mililiters":(inp,240,0,"ml"),
    "Meters-Inches":(inp,39.3701,0,"inch"),
    "Grams-Ounces":(inp,0.035274,0,"oz")
}
    if selected_conversion in conversions:
        result = conversion(*conversions[selected_conversion])
        result_label.config(text=result)
        


def perform_reversed_conversion():
    try:
        # Input from interface
        inp = float(input_entry.get())
    except ValueError:
        result_label.config(text="Invalid input")
        return

    # Selecting option from reversed conversion options dictionary
    selected_reversed_conversion = reverse_conversion_options.get()

    reversed_conversions={
    "Fahrenheit-Celsius":(inp, 5/9, 32,"C"),
    "Mililiters-Cups":(inp,0.004, 0, "cups"),
    "Inches-Meters":(inp, 0.0254,0, "m"),
    "Ounces-Grams":(inp,28.3495,0,"g")
    }

    if selected_reversed_conversion in reversed_conversions:
        result = reverse_conversion(*reversed_conversions[selected_reversed_conversion])
        result_label.config(text=result)

# Since the conversion and reversed conversion options are in the same placement, we need to hide one while the other operates
def toggle_combobox():
    # If conversion options is already mapped when we press the reverse button
    if conversion_options.winfo_ismapped():
        # Hide conversion options
        conversion_options.grid_forget()
        # Display reverse conversion options and update the convert button
        reverse_conversion_options.grid(row=1, column=1)
        convert_button.config(command=perform_reversed_conversion)
    else:
        # Hide reversed conversion options
        reverse_conversion_options.grid_forget()
        # Display conversion options and update the convert button
        conversion_options.grid(row=1, column=1)
        convert_button.config(command=perform_conversion)

# Interface
root = tk.Tk()
root.title("Unit converter")
root.geometry("300x200")

tk.Label(root, text="Value: ").grid(row=0, column=0)
input_entry = tk.Entry(root, width=20, borderwidth= 5, bg="#6E548E", fg="#D6BEDA")
input_entry.grid(row=0,column = 1)

tk.Label(root, text="From-to: ").grid(row=1,column=0)

conversion_options = ttk.Combobox(root, values=[
    "Celsius-Fahrenheit",
    "Cups-Mililiters",
    "Meters-Inches",
    "Grams-Ounces"
])
conversion_options.grid(row=1,column=1)

reverse_conversion_options = ttk.Combobox(root, values=[
    "Fahrenheit-Celsius",
    "Mililiters-Cups",
    "Inches-Meters",
    "Ounces-Grams"
])

reverse_button = tk.Button(root, text="Reverse",command= toggle_combobox )
reverse_button.grid(row=2,column=1)

convert_button = tk.Button(root, text="Convert", command= perform_conversion )
convert_button.grid(row=3,column=1)

result_label = tk.Label(root,text='',font=("Arial", 12, "bold"))
result_label.grid(row=4, column=1)

root.mainloop()