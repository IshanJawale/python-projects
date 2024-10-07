# Import Module
from tkinter import *

# Create Object
root = Tk()

# specify size of window.
root.geometry("400x400")

# Remove text from label

def remove_text():
	label.config(text="")

# Create Label
label = Label(root, text="Hello World!", font="BOLD")
label.pack()

# Create Delete Button
Button(root, text="Delete", command=remove_text).pack()

# Execute Tkinter
root.mainloop()
