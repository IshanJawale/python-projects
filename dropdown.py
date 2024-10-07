from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Dropdown...")
root.iconbitmap('gojo.ico')
root.geometry("400x400")

def Show():
    Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Days in the week")

days = [
    "Monday", 
    "Teusday", 
    "Wedneday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
]

drop = OptionMenu(root, clicked, *days)
drop.pack()

Button(root, text="Show the Selection", command=Show).pack()
root.mainloop()