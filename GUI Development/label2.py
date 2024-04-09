from tkinter import *
root = Tk()
var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
var.set("Hey! How its going?")
label.pack()
root.mainloop()
