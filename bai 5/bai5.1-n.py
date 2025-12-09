import tkinter as tk

root = tk.Tk()
root.title("Phan mem nho của Nhan")
root.geometry("300x150")

label = tk.Label(root, text="Xin chao ban Nhan!", font=("Arial", 16), fg="blue")
label.pack(pady=40)

root.mainloop()
