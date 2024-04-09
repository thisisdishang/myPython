import tkinter
import tkinter.messagebox
top = tkinter.Tk()
top.geometry("200x250")


def helloCallBack():
    tkinter.messagebox.showinfo("Welcome User", "Welcome Home Genesis")


B = tkinter.Button(top, text="Entry", command=helloCallBack)
B.pack()
top.mainloop()
