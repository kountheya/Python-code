import tkinter as tk
import math

def button_click(value):
    """Handles button clicks for all calculator buttons."""
    current_text = entry_field.get()
    
    if value == "C":
        # Clear the input field
        entry_field.delete(0, tk.END)
    elif value == "⌫":
        # Remove the last character in the input field (backspace)
        entry_field.delete(len(current_text) - 1)
    elif value == "=":
        # Evaluate the expression entered by the user
        try:
            result = eval(current_text)
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Error")
    elif value == "x²":
        # Square the current number
        try:
            num = float(current_text)
            result = num ** 2
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Error")
    elif value == "√x":
        # Calculate the square root of the current number
        try:
            num = float(current_text)
            if num < 0:
                raise ValueError("Cannot take square root of a negative number.")
            result = math.sqrt(num)
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Error")
    elif value == "%":
        # Calculate percentage
        try:
            num = float(current_text)
            result = num / 100
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(result))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Error")
    elif value == "±":
        # Toggle the sign (positive/negative)
        try:
            num = float(current_text)
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, str(-num))
        except Exception:
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, "Error")
    else:
        # Append the button value to the input field
        entry_field.insert(tk.END, value)

# Initialize the main window
root = tk.Tk()
root.title("Fully Functional Calculator")

# Entry field for input and output
entry_field = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Define button layout
buttons = [
    ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("±", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3),
    ("x²", 6, 0), ("√x", 6, 1), ("(", 6, 2), (")", 6, 3),
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    if text:  # Ignore empty cells
        button = tk.Button(
            root, text=text, font=("Arial", 18), borderwidth=1, relief="raised",
            command=lambda value=text: button_click(value), width=5, height=2
        )
        button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
