import tkinter as tk

root = tk.Tk()
root.title("Phần mềm nhỏ của Hiệp")
root.geometry("300x150")

label = tk.Label(root, text="Xin chào bạn Hiệp!", font=("Arial", 16), fg="blue")
label.pack(pady=40)

root.mainloop()
