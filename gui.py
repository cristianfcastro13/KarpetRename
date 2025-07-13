import tkinter as tk
from tkinter import filedialog

# Defining window attributes
root = tk.Tk()
root.title("Karpet Renamer")
root.iconbitmap("icon.ico")
root.resizable(False, False)
root.geometry("400x400")
root.config(bg="#FFFFFF")

# Defining variables for the GUI
folder_path = tk.StringVar()
prefix_entry = tk.Entry(root)
suffix_entry = tk.Entry(root)
is_dry_run = tk.BooleanVar()

# Retrieving user inputs from the GUI
user_prefix = prefix_entry.get()
user_suffix = suffix_entry.get()
should_dry_run = is_dry_run.get()


# Function to open a folder dialog and set the selected directory to the StringVar
def open_folder_dialog():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        folder_path.set(selected_directory)

# Creating all windows widgets and packing them in
browse_button = tk.Button(root, text="Browse", command= open_folder_dialog)
my_label = tk.Label(root, textvariable=folder_path)
dry_run_check = tk.Checkbutton(root, text='Dry Run Mode', variable=is_dry_run)
prefix_entry = tk.Entry(root, width=20, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
suffix_entry = tk.Entry(root, width=20, font=("Arial", 12), bg="#FFFFFF", fg="#000000")
browse_button.grid(row=0, column=0)
my_label.grid(row=0, column=1)
dry_run_check.grid(row=3, column=0)
prefix_entry.grid(row=1, column=0)
suffix_entry.grid(row=2, column=0)



root.mainloop()