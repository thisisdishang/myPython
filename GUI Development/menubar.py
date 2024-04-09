from tkinter import *
top=Tk()

def hello():
    print("Hello")

menubar=Menu(top)
menubar.add_command(label="Hello",command=hello)
menubar.add_command(label="Quit",command=top.quit)
top.config(menu=menubar)
top.mainloop()