import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to remove the selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Function to clear all tasks
def clear_tasks():
    response = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if response == 1:
        tasks_listbox.delete(0, tk.END)

# Function to save tasks to a text file
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Tasks Saved", "Tasks have been saved successfully!")

# Function to load tasks from a text file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                tasks_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "No saved tasks found!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

# Task entry box and add button
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

# Task list box to display tasks
tasks_listbox = tk.Listbox(root, height=10, width=40)
tasks_listbox.pack(pady=10)

# Control buttons (Delete, Clear, Save, Load)
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Tasks", width=15, command=clear_tasks)
clear_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", width=15, command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", width=15, command=load_tasks)
load_button.pack(pady=5)

# Start GUI loop
root.mainloop()
