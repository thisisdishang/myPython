from tkinter import *
import tkinter.messagebox
import tkinter
top = tkinter.Tk()
Checkvar1 = IntVar()
Checkvar2 = IntVar()
C1 = Checkbutton(top, text="Music", variable=Checkvar1,
                 onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="Video", variable=Checkvar2,
                 onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()
top.mainloop()
