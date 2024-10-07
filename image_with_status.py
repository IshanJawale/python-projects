from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image With Status...")
root.iconbitmap('gojo.ico')



my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/img6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/img7.jpg"))
my_img8= ImageTk.PhotoImage(Image.open("images/img8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/img9.jpg"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9]
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)  # bd for border, relief for sunken label, anchor to east
my_label = Label(image=my_img1, padx=40, pady=40)
my_label.grid(row=0, column=0, columnspan=3)

def buttonForward(image_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label = Label(root, image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: buttonForward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: buttonBack(image_number-1))
    if image_number == 9:
        button_forward = Button(root,text=">>", state=DISABLED)
    
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def buttonBack(image_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    
    my_label = Label(root, image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: buttonForward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: buttonBack(image_number-1))
    if image_number == 1:
        my_label.grid_forget()
        button_back = Button(root, text="<<", state=DISABLED) 
    
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=buttonBack, state=DISABLED)
button_exit = Button(root, text="Exit Viewer", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: buttonForward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # Stretched from west to east
root.mainloop()