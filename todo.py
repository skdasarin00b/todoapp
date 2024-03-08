import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pickle  # Import the pickle module

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable To-Do App")
        self.root.geometry("400x500")
        # ... (rest of your code)

        # List to store tasks
        self.tasks = []

        # Style for buttons
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))

        # Entry for adding tasks
        self.task_entry = tk.Entry(root, font=("Helvetica", 12))
        self.task_entry.pack(fill=tk.X, padx=20, pady=10)

        # Button to add tasks
        self.add_icon = self.resize_icon("add_icon.png", 20, 20)
        add_button = ttk.Button(root, text="Add Task", command=self.add_task, image=self.add_icon, compound=tk.RIGHT)
        add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#a6a6a6")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Button to remove selected task
        self.remove_icon = self.resize_icon("remove_icon.png", 20, 20)
        remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task, image=self.remove_icon, compound=tk.LEFT)
        remove_button.pack(pady=5)

        # Bind mouse dragging to resize the window
        self.root.bind("<B1-Motion>", self.resize_window)

    def resize_icon(self, filename, width, height):
        original_image = Image.open(filename)
        resized_image = original_image.resize((width, height))
        icon = ImageTk.PhotoImage(resized_image)
        return icon

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
            # Save data after adding a task
            self.save_data()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            removed_task = self.tasks.pop(selected_index)
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("Task Removed", f"Removed Task: {removed_task}")
            # Save data after removing a task
            self.save_data()
        # ... (rest of your code)

    def resize_window(self, event):
        x, y = event.x_root, event.y_root
        width = x - self.root.winfo_rootx()
        height = y - self.root.winfo_rooty()
        self.root.geometry(f"{width}x{height}")
        # ... (rest of your code)

    def save_data(self):
        # Saving data to a local file using pickle
        with open("todo_data.pkl", "wb") as file:
            pickle.dump(self.tasks, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
