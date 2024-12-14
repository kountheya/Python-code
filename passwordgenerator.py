import tkinter as tk
import random
import string

# Function to generate the password
def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Function to be called when the generate button is clicked or Enter is pressed
def on_generate_click(event=None):  # event=None allows calling it from the Enter key
    try:
        # Get the length from the entry widget
        length = int(length_entry.get())
        # Generate the password
        password = generate_password(length)
        # Display the generated password
        password_label.config(text=f"Generated Password: {password}")
        # Enable the copy button
        copy_button.config(state=tk.NORMAL)
    except ValueError:
        password_label.config(text="Please enter a valid number.")
        # Disable the copy button if input is invalid
        copy_button.config(state=tk.DISABLED)

# Function to copy the password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(password_label.cget("text").replace("Generated Password: ", ""))  # Copy password text
    root.update()  # Update the clipboard
    status_label.config(text="Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")  # Window size

# Create a title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 20))
title_label.pack(pady=20)

# Create an entry label and input field for the password length
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Bind the "Enter" key to the on_generate_click function
length_entry.bind("<Return>", on_generate_click)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=on_generate_click)
generate_button.pack(pady=20)

# Label to display the generated password
password_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12), wraplength=450, justify="left")
password_label.pack(pady=10)

# Create a button to copy the password to the clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

# Label to show status (like "Password copied to clipboard")
status_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
status_label.pack(pady=5)

# Run the main event loop
root.mainloop()
