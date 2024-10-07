from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# define your buttons

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def buttonClear():
    e.delete(0, END) 

def buttonAdd():
    first_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = int(first_number)
    e.delete(0, END)


def buttonSub():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def buttonMul():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def buttonDiv():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)

def buttonEqual():
    second_number = e.get()
    e.delete(0, END)
    if(math == "Addition"):
        e.insert(0, int(f_num) + int(second_number))
    elif(math == "Subtraction"):
        e.insert(0, f_num - int(second_number))
    elif(math == "Multiplication"):
        e.insert(0, f_num * int(second_number))
    elif(math == "Division"):
        e.insert(0, f_num / int(second_number))
    elif(math == "Root"):
        e.insert(0, f_num / int(second_number))
    elif(math == "Square"):
        e.insert(0, f_num / int(second_number))

# make buttons 

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

button_clear = Button(root, text="Clear", padx=76, pady=20, command=buttonClear)
button_add = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
button_sub = Button(root, text="-", padx=40, pady=20, command=buttonSub)
button_mul = Button(root, text="*", padx=40, pady=20, command=buttonMul)
button_div = Button(root, text="/", padx=40, pady=20, command=buttonDiv)
button_equal = Button(root, text="=", padx=86, pady=20, command=buttonEqual)

# Put buttons on the screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_clear.grid(row=4, column=1, columnspan=2)

button_quit = Button(root,padx=105, pady=10, text="Exit Program", command=root.quit)
button_quit.grid(row=7, column=0, columnspan=3)


root.mainloop()