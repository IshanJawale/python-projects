from tkinter import *
root = Tk()
root.title("Bookings...")
def ifClicked():
    print("The button is clicked!!!")
    Label(root, text="The button is clicked!!!").pack()
Button(root, text="Click here!", command=ifClicked).pack()

root.mainloop()