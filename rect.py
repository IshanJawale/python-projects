from tkinter import Canvas
from tkinter import *

window = Tk()
window.title("Canvas") # giving title to window
window.config(bg = "grey")
window.geometry("400x400") # setting up the geometry
window.resizable(False, False) # disabling the resize option from x-y sides

my_canvas = Canvas(width = 30, height = 20, bg = "white") # canvas object to create canvas
my_canvas.grid(row=4, column=0, pady = 20) # padding it 20 pixels below from margin of window
my_canvas2 = Canvas(width=20, height=0, bg="white")
my_canvas2.grid(row=4, column=1)
window.mainloop()