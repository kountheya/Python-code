import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Sample contact list (could be a database in a real application)
contacts = []

# Function to add a new contact
def add_contact(event=None):  # Allow 'Enter' key to trigger this function
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields.")

# Function to clear the input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to display the contacts in the listbox
def display_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search contacts by name or phone
def search_contact(event=None):  # Allow 'Enter' key to trigger this function
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    
    filtered_contacts = [contact for contact in contacts if search_term in contact["name"].lower() or search_term in contact["phone"]]
    for contact in filtered_contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to delete a contact
def delete_contact():
    selected_index = listbox_contacts.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        contacts.remove(contact)
        display_contacts()
        messagebox.showinfo("Success", f"Contact {contact['name']} deleted.")
    else:
        messagebox.showwarning("Select Error", "Please select a contact to delete.")

# Function to update contact details
def update_contact():
    selected_index = listbox_contacts.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

        entry_name.insert(0, contact["name"])
        entry_phone.insert(0, contact["phone"])
        entry_email.insert(0, contact["email"])
        entry_address.insert(0, contact["address"])

        contacts.remove(contact)
        display_contacts()
    else:
        messagebox.showwarning("Select Error", "Please select a contact to update.")

# Creating the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x600")  # Set window size
root.config(bg="#f4f4f9")

# Styling
style = ttk.Style()
style.configure("TLabel", background="#f4f4f9", font=("Arial", 12))
style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))
style.map("TButton", background=[("active", "#45a049")])

# Labels and entry fields for adding new contacts
label_name = ttk.Label(root, text="Name")
label_name.pack(pady=5)

entry_name = ttk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

label_phone = ttk.Label(root, text="Phone")
label_phone.pack(pady=5)

entry_phone = ttk.Entry(root, font=("Arial", 12))
entry_phone.pack(pady=5)

label_email = ttk.Label(root, text="Email")
label_email.pack(pady=5)

entry_email = ttk.Entry(root, font=("Arial", 12))
entry_email.pack(pady=5)

label_address = ttk.Label(root, text="Address")
label_address.pack(pady=5)

entry_address = ttk.Entry(root, font=("Arial", 12))
entry_address.pack(pady=5)

# Buttons for adding, updating, and deleting contacts
button_add = ttk.Button(root, text="Add Contact", command=add_contact)
button_add.pack(pady=10)

button_update = ttk.Button(root, text="Update Contact", command=update_contact)
button_update.pack(pady=5)

button_delete = ttk.Button(root, text="Delete Contact", command=delete_contact)
button_delete.pack(pady=5)

# Search feature
label_search = ttk.Label(root, text="Search (by name or phone)")
label_search.pack(pady=10)

entry_search = ttk.Entry(root, font=("Arial", 12))
entry_search.pack(pady=5)

button_search = ttk.Button(root, text="Search", command=search_contact)
button_search.pack(pady=10)

# Bind the 'Enter' key to add and search functions
root.bind('<Return>', add_contact)
root.bind('<Return>', search_contact)

# Listbox to display the contacts
listbox_contacts = tk.Listbox(root, width=50, height=10, font=("Arial", 12), selectmode=tk.SINGLE, bg="#f9f9f9", relief="solid")
listbox_contacts.pack(pady=20)

# Initial display of contacts (empty initially)
display_contacts()

# Run the application
root.mainloop()
