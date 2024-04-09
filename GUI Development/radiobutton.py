from cProfile import label
from tkinter import *


def selection():
    selection = "You selected the option "+str(radio.get())
    label.config(text=selection)


top = Tk()
top.geometry("300x150")
radio = IntVar()
lbl = Label(text="Programming Language:-")
lbl.pack()
R1 = Radiobutton(top, text="C", variable=radio, value=1, command=selection)
R1.pack(anchor=W)
R2 = Radiobutton(top, text="Dart", variable=radio, value=2, command=selection)
R2.pack(anchor=W)
R3 = Radiobutton(top, text="Python", variable=radio,
                 value=3, command=selection)
R3.pack(anchor=W)
label = Label(top)
label.pack()
top.mainloop()
