from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Frames in Tkinter")
root.iconbitmap("gojo.ico")

frame = LabelFrame(root, text="This is Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

frame_button1 = Button(frame, text="Don't Click Here!")
frame_button1.grid(row=0, column=0)     # you can use pack for the frame and grid in side the frame and it will not show an error
frame_button2 = Button(frame, text="Click Here!")
frame_button2.grid(row=1, column=1)

root.mainloop()