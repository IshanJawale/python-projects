from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Check Boxes...")
root.iconbitmap('gojo.ico')
root.geometry("400x400")

def afterChecked():
    Label(root, text=var.get()).pack()

def afterChecked_():
    my_label = Label(root, text=var_.get())
    my_label.pack_forget()
    my_label.pack()


var = IntVar()
c = Checkbutton(root, text="check this button", variable=var, command=afterChecked)
c.pack()

var_ = StringVar()
c_ = Checkbutton(root, text="For string output", variable=var_, onvalue="on", offvalue="off", command=afterChecked_)
c_.deselect()   # for some reason the checkbox is already checked by default for StirngVar() so we have to deselect it...
c_.pack()

root.mainloop()