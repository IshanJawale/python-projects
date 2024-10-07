from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Code Window...")
root.iconbitmap('E:\Ishan\Python_Projects\Python Project\gojo.ico')

my_img = ImageTk.PhotoImage(Image.open("gojo.jpg"))
my_label = Label(image=my_img)
my_label.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()