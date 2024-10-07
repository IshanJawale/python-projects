from tkinter import *
root = Tk()
# Creating a wigdet
myLabel1 = Label(root, text = "Hello")
myLabel2 = Label(root, text = "My name is Ishan Jawale")
# myLabel1 = Label(root, text = "Hello").grid(row=0, column=0)
# myLabel2 = Label(root, text = "My name is Ishan Jawale").grid(row=1, column=1)
# can do the above also since python is object oriented
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
root.mainloop()