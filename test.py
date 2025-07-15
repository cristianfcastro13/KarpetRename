import tkinter as tk

window = tk.Tk()

window.title("Test Window")
randomentry = tk.Entry(window)
randomentry.config(width=20, font=("Ink Free", 70), bg="#FFFFFF", fg="#000000")
randomentry.pack()
window.mainloop()