from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File Finder...")
root.iconbitmap('gojo.ico')



def openImage():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="E:\Ishan\Python_Projects\Python Project", title="Open a PDF", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("All files", "*.*")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_img).pack()

Button(root, text="Open an Image", command=openImage).pack()

root.mainloop()