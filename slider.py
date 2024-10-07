from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Slider...")
root.iconbitmap('gojo.ico')
def displaySliderNumber(var):
    Label(root, text=horizontal.get()).grid(row=3, column=0)
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=200, to=1000, command=displaySliderNumber)
vertical.grid(row=0, column=0)

horizontal = Scale(root, from_=200, to=1000, orient=HORIZONTAL, command=displaySliderNumber) 
horizontal.grid(row=1, column=0)

Button(root, text="Display the slider status", command=lambda: displaySliderNumber(horizontal.get())).grid(row=2, column=0)

root.mainloop()