from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="I clicked!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", state=DISABLED) # disables the button so that you cannot click it
myButton2 = Button(root, text="Click Me!2", padx=50, pady=50) # padx and pady for width and height of the button in each axis
myButton3 = Button(root, text="Click for text...", command=myClick, fg="blue", bg="black") # command calls the function
# fg for the font colour and bg for the background colour
myButton.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()