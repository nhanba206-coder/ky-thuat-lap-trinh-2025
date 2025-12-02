from tkinter import *

root = Tk()
root.title("Radio Button Example")

v = IntVar()
v.set(1)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def show_choice():
    print(v.get())

label = Label(root, text="Choose your favourite programming language:")
label.pack(anchor="w")

for lang, val in languages:
    Radiobutton(root, text=lang, variable=v, value=val).pack(anchor="w")

btn = Button(root, text="Show", command=show_choice)
btn.pack()

root.mainloop()
