from tkinter import *
root = Tk()

e = Entry(root, width=50, bg="black", fg="blue", borderwidth=50)
e.pack()
e.insert(0, "Enter your name: ") # select it and rewrite your name
def myClick():
    hello = "Hello " + e.get() # just to make the text field more clear
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Display", command=myClick, fg="blue", bg="black") 

myButton.pack()

root.mainloop()