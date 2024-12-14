import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

# To-Do List Application
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x600")
        self.root.config(bg="#f0f0f0")

        # Create the frame for tasks
        self.task_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.task_frame.pack(pady=10, fill="both", expand=True)

        # Task Entry and Buttons
        self.entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=30, font=("Arial", 14))
        self.task_entry.pack(side="left", padx=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = tk.Button(
            self.entry_frame, text="Add Task", font=("Arial", 12), command=self.add_task
        )
        self.add_button.pack(side="left", padx=5)

        self.remove_button = tk.Button(
            self.entry_frame, text="Remove Task", font=("Arial", 12), command=self.delete_task
        )
        self.remove_button.pack(side="left", padx=5)

        self.action_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.action_frame.pack(pady=10)

        self.mark_done_button = tk.Button(
            self.action_frame, text="Mark as Done", font=("Arial", 12), bg="#d3ffd3", command=self.mark_complete
        )
        self.mark_done_button.pack(side="left", padx=10)

        self.mark_not_done_button = tk.Button(
            self.action_frame, text="Mark as Not Done", font=("Arial", 12), bg="#ffd3d3", command=self.mark_not_complete
        )
        self.mark_not_done_button.pack(side="left", padx=10)

        self.save_button = tk.Button(
            self.root, text="Save Tasks", font=("Arial", 12), command=self.save_tasks
        )
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(
            self.root, text="Load Tasks", font=("Arial", 12), command=self.load_tasks
        )
        self.load_button.pack(pady=5)

        self.clear_button = tk.Button(
            self.root, text="Clear All Tasks", font=("Arial", 12), command=self.clear_tasks
        )
        self.clear_button.pack(pady=5)

        # Task List
        self.task_list = tk.Listbox(
            self.task_frame,
            width=50,
            height=20,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            bg="#fff",
            fg="#000",
        )
        self.task_list.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Context Menu for Deleting Tasks
        self.task_list.bind("<Button-3>", self.show_context_menu)
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Mark as Complete", command=self.mark_complete)
        self.context_menu.add_command(label="Mark as Not Completed", command=self.mark_not_complete)
        self.context_menu.add_command(label="Delete Task", command=self.delete_task)

        # Status Bar
        self.status_bar = tk.Label(self.root, text="0 tasks", bg="#f0f0f0", font=("Arial", 10), anchor="w")
        self.status_bar.pack(fill="x", side="bottom")

        self.update_status()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.task_list.insert(tk.END, f"{task} (Added: {timestamp})")
            self.task_list.itemconfig(tk.END, {'bg': '#ffffff'})
            self.task_entry.delete(0, tk.END)
            self.update_status()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
            self.update_status()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def mark_complete(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(tk.END, f"[Completed] {task}")
            self.task_list.itemconfig(tk.END, {'bg': '#d3ffd3'})  # Green background for completed tasks
            self.update_status()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def mark_not_complete(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(tk.END, f"[Not Completed] {task}")
            self.task_list.itemconfig(tk.END, {'bg': '#ffd3d3'})  # Red background for not completed tasks
            self.update_status()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if file_path:
            with open(file_path, "w") as file:
                tasks = self.task_list.get(0, tk.END)
                file.writelines(task + "\n" for task in tasks)
            messagebox.showinfo("Info", "Tasks saved successfully!")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.task_list.delete(0, tk.END)
            with open(file_path, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_list.insert(tk.END, task.strip())
            self.update_status()

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_list.delete(0, tk.END)
            self.update_status()

    def update_status(self):
        task_count = self.task_list.size()
        self.status_bar.config(text=f"{task_count} tasks")

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
