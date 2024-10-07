from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Radio Buttons...")
root.iconbitmap('gojo.ico')

var = IntVar()  # if value = "1" then it is StrVar, and so on...
var.set(2)  # by default the value of var is set to 2 and the 2nd option is selected


def clicked(value):

    var.set(value)
    label = Label(root, text=var.get())
    label.pack_forget()
    label.pack()

Radiobutton(root, text="Option 1", variable=var, value=1, command=lambda: clicked(var.get())).pack()
Radiobutton(root, text="Option 1", variable=var, value=2, command=lambda: clicked(var.get())).pack()

label = Label(root, text=var.get())
label.pack()
root.mainloop()