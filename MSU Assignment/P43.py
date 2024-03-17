# Write a python program to create calculator using Tkinter.

import tkinter as tk

def add_digit(digit):
    current = display_var.get()
    display_var.set(current + digit)

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Variable to hold the expression
display_var = tk.StringVar()
display_var.set("")

# Entry widget to display the expression and result
display_entry = tk.Entry(root, textvariable=display_var, justify="right")
display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Function to handle button clicks
def button_click(button):
    if button == '=':
        calculate()
    elif button == 'C':
        clear_display()
    else:
        add_digit(button)

# Add buttons to the window
row, col = 1, 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button:
              button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI
root.mainloop()
