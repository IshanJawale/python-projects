from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Radio Button List...")
root.iconbitmap('gojo.ico')

theStrongestInJujutsuKaisen = [   # tuple inside list to make many radio buttons easily
    ("Itadori", "Itadori is the strongest character!!!"),
    ("Gojo", "Gojo is the strongest character!!!"),
    ("Sukuna", "Sukuna is the strongest character!!!"),
    ("Geto", "Geto is the strongest character!!!")
]

def clicked(value):
    juju.set(value)
    label = Label(root, text=juju.get())
    label.pack()

juju = StringVar()
juju.set("Gojo is the strongest character!!!")

for character, strongest in theStrongestInJujutsuKaisen:
    Radiobutton(root, text=character, variable=juju, value=strongest, command=lambda: clicked(juju.get())).pack(anchor=W)

label = Label(root, text=juju.get())
label.pack()

my_button = Button(root, text="Current Strongest...", command=lambda: clicked(juju.get()))
my_button.pack()

root.mainloop()