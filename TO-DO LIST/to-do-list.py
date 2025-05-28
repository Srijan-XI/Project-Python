import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

tasks = []

def update_task_list():
    listbox_tasks.delete(*listbox_tasks.get_children())
    selected_category = category_filter.get()
    for idx, task in enumerate(tasks):
        if selected_category == "All" or task["category"] == selected_category:
            checked = "✓" if task["completed"] else ""
            listbox_tasks.insert("", "end", iid=idx, values=(checked, task["description"], task["due_date"], task["category"]))

def add_task():
    desc = entry_desc.get().strip()
    due = entry_due.get().strip()
    category = category_entry.get()
    if not desc or not due:
        messagebox.showwarning("Input Error", "Task description and due date required.")
        return
    try:
        datetime.strptime(due, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Use YYYY-MM-DD format for due date.")
        return
    task = {
        "description": desc,
        "due_date": due,
        "category": category if category else "General",
        "completed": False
    }
    tasks.append(task)
    entry_desc.delete(0, tk.END)
    entry_due.delete(0, tk.END)
    category_entry.set("General")
    update_task_list()

def delete_task():
    selected = listbox_tasks.selection()
    if not selected:
        messagebox.showwarning("Delete Error", "Select a task to delete.")
        return
    for idx in reversed([int(iid) for iid in selected]):
        tasks.pop(idx)
    update_task_list()

def toggle_complete():
    selected = listbox_tasks.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a task to toggle complete.")
        return
    for iid in selected:
        tasks[int(iid)]["completed"] = not tasks[int(iid)]["completed"]
    update_task_list()

def clear_tasks():
    if messagebox.askyesno("Confirmation", "Clear all tasks?"):
        tasks.clear()
        update_task_list()

def filter_tasks(*args):
    update_task_list()

window = tk.Tk()
window.title("To-Do List Manager")
window.geometry("1000x600")
window.configure(bg="#f0f0f0")
window.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=("Segoe UI", 12), rowheight=30)
style.configure("Treeview.Heading", font=("Segoe UI", 13, "bold"))
style.map("Treeview", background=[("selected", "#cce5ff")])

header = tk.Label(window, text="To-Do List Application", font=("Segoe UI", 20, "bold"), bg="#f0f0f0", fg="#333")
header.pack(pady=10)

top_frame = tk.Frame(window, bg="#f0f0f0")
top_frame.pack(pady=5)

tk.Label(top_frame, text="Task", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
entry_desc = tk.Entry(top_frame, font=("Segoe UI", 12), width=25)
entry_desc.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Due Date (YYYY-MM-DD)", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=2, padx=5)
entry_due = tk.Entry(top_frame, font=("Segoe UI", 12), width=15)
entry_due.grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Category", font=("Segoe UI", 12), bg="#f0f0f0").grid(row=0, column=4, padx=5)
category_entry = ttk.Combobox(top_frame, font=("Segoe UI", 12), width=12)
category_entry['values'] = ["Work", "Study", "Home", "Urgent", "General"]
category_entry.set("General")
category_entry.grid(row=0, column=5, padx=5)

btn_add = tk.Button(top_frame, text="Add Task", font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white", width=12, command=add_task)
btn_add.grid(row=0, column=6, padx=10)

columns = ("Done", "Task", "Due Date", "Category")
listbox_tasks = ttk.Treeview(window, columns=columns, show="headings", height=10)
for col in columns:
    listbox_tasks.heading(col, text=col)
    listbox_tasks.column(col, anchor="center", width=180)
listbox_tasks.pack(pady=15)

bottom_frame = tk.Frame(window, bg="#f0f0f0")
bottom_frame.pack(pady=5)

btn_complete = tk.Button(bottom_frame, text="Toggle Complete", font=("Segoe UI", 11), bg="#007bff", fg="white", width=15, command=toggle_complete)
btn_complete.grid(row=0, column=0, padx=10)

btn_delete = tk.Button(bottom_frame, text="Delete Task", font=("Segoe UI", 11), bg="#dc3545", fg="white", width=15, command=delete_task)
btn_delete.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(bottom_frame, text="Clear All", font=("Segoe UI", 11), bg="#ffc107", fg="black", width=15, command=clear_tasks)
btn_clear.grid(row=0, column=2, padx=10)

tk.Label(bottom_frame, text="Filter by Category", font=("Segoe UI", 11), bg="#f0f0f0").grid(row=0, column=3, padx=10)
category_filter = ttk.Combobox(bottom_frame, font=("Segoe UI", 11), width=12)
category_filter['values'] = ["All", "Work", "Study", "Home", "Urgent", "General"]
category_filter.set("All")
category_filter.grid(row=0, column=4, padx=5)
category_filter.bind("<<ComboboxSelected>>", filter_tasks)

update_task_list()
window.mainloop()
