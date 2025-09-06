import tkinter as tk
from tkinter import ttk

def conversion(value1,convert1, add, unit2,inp):
    
    inp = input("Enter your value in %s: "% value1)
    inp = float(inp)
    result1 = inp*convert1 + add
    return f"{result1:.2f} {unit2}"

def reverse_conversion(value2,convert2,add,unit1):
    inp = input("Enter your value in %s: " % value2)
    inp = float(inp)
    result2 = (inp - add)*convert2 
    return f"{result2:.2f} {unit1}"

def perform_conversion():
    inp = input_entry.get()
    selected_conversion = conversion_options.get()

    conversions={
    "Celsius-Fahrenheit":("Fahrenheit", 2.5, 0.4, 32, "C",inp),
    "Cups-Mililiters":("ml",0.004, 0, "cups",inp),
    "Meters-Inches":("inch", 0.0254,0, "m",inp),
    "Grams-Ounces":("oz",28.3495,0,"g",inp)
}
    if selected_conversion and inp.replace('.', '', 1).isdigit():
        value1, convert1, add, unit2,inp = conversions[selected_conversion]
        result1 = conversion(value1, convert1, add, unit2, inp)
        result1_label.config(text=result1)
        print(result1)


def perform_reversed_conversion():
    inp = input_entry.get()
    selected_reversed_conversion = reverse_conversion_options.get()

    reversed_conversions={
    "Fahrenheit-Celsius":("Celsius",2.5,32,"F",inp),
    "Mililiters-Cups":("cups",250,0,"ml",inp),
    "Inches-Meters":("m",39.3701,0,"inch",inp),
    "Ounces-Grams":("g",0.035274,0,"oz",inp)
    }
    if selected_reversed_conversion and inp.replace('.', '', 1).isdigit():
        value2, convert2, add, unit1,inp = reversed_conversions[selected_reversed_conversion]
        result2 = conversion(value2, convert2, add, unit1,inp)
        result2_label.config(text=result2)
        print(result2)

def display_reverse_options():
    conversion_options.grid_forget()
    reverse_conversion_options.grid(row=1,column=1)
    perform_reversed_conversion()

def toggle_combobox():
    if conversion_options.winfo_ismapped():
        conversion_options.grid_forget()
        reverse_conversion_options.grid(row=1, column=1)
    else:
        reverse_conversion_options.grid_forget()
        conversion_options.grid(row=1, column=1)

root = tk.Tk()
root.title("Unit converter")
root.geometry("250x275")

input_value = tk.Label(root, text="Value: ")
input_entry = tk.Entry(root, width=20, borderwidth= 5, bg="#6E548E", fg="#D6BEDA")
from_to_unit_label = tk.Label(root, text="From-to: ")
conversion_options = ttk.Combobox(root, values=["Celsius-Fahrenheit","Cups-Mililiters","Meters-Inches","Grams-Ounces"])
reverse_button = tk.Button(root, text="Reverse",command= display_reverse_options )
convert_button = tk.Button(root, text="Convert", command= perform_conversion )
result1_label = tk.Label(root,text='')
result2_label = tk.Label(root, text='')
reverse_conversion_options = ttk.Combobox(root, values=["Fahrenheit-Celsius","Mililiters-Cups","Inches-Meters","Ounces-Grams"])

reverse_conversion_options.grid(row=1,column=1)
input_value.grid(row=0, column=0)
input_entry.grid(row = 0, column = 1)
from_to_unit_label.grid(row=1, column=0)
conversion_options.grid(row=1,column=1)
reverse_button.grid(row=2,column=1)
convert_button.grid(row=3,column=1)
result1_label.grid(row=4, column=1)
result2_label.grid(row=4, column=1)

root.mainloop()