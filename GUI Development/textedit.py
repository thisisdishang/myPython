from tkinter import *
def onclick():
    pass

root=Tk()
text=Text(root)
text.insert(INSERT,"Hello...")
text.insert(END,"Bye Bye...")
text.pack()

text.tag_add("here","1.0","1.5")
text.tag_add("start","1.8","1.15")
text.tag_config("here",background="blue",foreground="white")
text.tag_config("start",background="red",foreground="black")
root.mainloop()