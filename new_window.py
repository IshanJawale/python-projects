from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Base Window...")
root.iconbitmap('gojo.ico')
def openNewWindow():
    global my_image
    top = Toplevel()
    top.title("New Window...")
    top.iconbitmap('gojo.ico')
    lbl = Label(top, text="This is a new window!").pack()
    my_image = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
    my_label = Label(top, image=my_image).pack()
    Button(top, text="Close the new Window", command=top.destroy).pack()
Button(root, text="Click to Open New window", command=openNewWindow, padx=5, pady=5, bd=5).pack()

root.mainloop()