import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.tasks = []

        self.label = tk.Label(root, text="To-Do List", font=("Arial", 15))
        self.label.pack(pady=20)

        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(pady=20)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=20)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=10)

        self.del_btn = tk.Button(root, text="Delete Task", command=self.del_task)
        self.del_btn.pack(pady=10)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task!")

    def del_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            messagebox.showwarning("Warning", "You must select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List App")
    app = TodoListApp(root)
    root.mainloop()
