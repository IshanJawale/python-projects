from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("Message Box...")
root.iconbitmap('gojo.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel

def Info():
    response = messagebox.showinfo("Welcome!!!", "Hello World!")
    Label(root, text=response).pack()   # prints ok (also on closing the popup by clicking the X button)
def Warn():   
    response = messagebox.showwarning("Welcome!!!", "Hello World!")
    Label(root, text=response).pack()   # prints ok (also on closing the popup by clicking the X button)
def Error():
    response = messagebox.showerror("Welcome!!!", "Hello World!")
    Label(root, text=response).pack()   # prints ok (also on closing the popup by clicking the X button)
def Question():
    response = messagebox.askquestion("Welcome!!!", "Hello World!")
    #Label(root, text=response).pack()      -- this prints yes for yes and no for no...
    if response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No...").pack()
def okCancel():
    response = messagebox.askokcancel("Welcome!!!", "Hello World!")
    #Label(root, text=response).pack()      -- this prints 1 for ok and 0 for cancel...
    if response == 1:
        Label(root, text="You Clicked Ok!").pack()
    else:
        Label(root, text="You Clicked Cancel...").pack()
def yesNo():
    response = messagebox.askyesno("Welcome!!!", "Hello World!")
    #Label(root, text=response).pack()       -- this prints 1 for yes and 0 for no...
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No...").pack()
def retryCancel():
    response = messagebox.askretrycancel("Welcome!!!", "Hello World!")
    #Label(root, text=response).pack()       -- this prints 1 for retry and 0 for cancel...
    if response == 1:
        Label(root, text="You Clicked Retry!").pack()
    else:
        Label(root, text="You Clicked Cancel...").pack()

Button(root, text="Info", command=Info).pack()
Button(root, text="Warning", command=Warn).pack()
Button(root, text="Error", command=Error).pack()
Button(root, text="Question", command=Question).pack()
Button(root, text="Ok Cancel", command=okCancel).pack()
Button(root, text="Yes No", command=yesNo).pack()
Button(root, text="Retry Cancel", command=retryCancel).pack()

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=10, pady=10)
Button(frame, text="Exit Program", command=root.quit, relief=SUNKEN).pack()

root.mainloop()