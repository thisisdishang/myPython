# Write a python program to create student registration form and collect the data provied by student in database.

from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="Question44"
)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE student (RollNo INT PRIMARY KEY, First_Name VARCHAR(255),Last_Name VARCHAR(255),Phone_Number VARCHAR(255),City VARCHAR(255))")
root = Tk()
root.title("Student Data")
root.geometry("500x500")
label1 = Label(root, text="RollNo", width=20, height=2).grid(row=0, column=0)
label2 = Label(root, text="First_Name", width=20,
               height=2).grid(row=1, column=0)
label3 = Label(root, text="Last_Name", width=20,
               height=2).grid(row=2, column=0)
label4 = Label(root, text="Phone_Number", width=20,
               height=2).grid(row=3, column=0)
label5 = Label(root, text="City", width=20, height=2).grid(row=4, column=0)
e1 = Entry(root, width=30, borderwidth=8)
e1.grid(row=0, column=1)
e2 = Entry(root, width=30, borderwidth=8)
e2.grid(row=1, column=1)
e3 = Entry(root, width=30, borderwidth=8)
e3.grid(row=2, column=1)
e4 = Entry(root, width=30, borderwidth=8)
e4.grid(row=3, column=1)
e5 = Entry(root, width=30, borderwidth=8)
e5.grid(row=4, column=1)

'''
def Register():
    RollNo = e1.get()
    dbRollNo = ""
    Select = "select count(*) from student where RollNo='%s'" % (RollNo)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbRollNo = i[0]

        if (int(RollNo) != int(dbRollNo)):
            Insert = "Insert into student (RollNo,First_Name,Last_Name,Phone_Number,City) values(%s,%s,%s,%s,%s)"
            First_Name = e2.get()
            Last_Name = e3.get()
            Phone_Number = e4.get()
            City = e5.get()
        if (First_Name != "" and Last_Name != "" and Phone_Number != "" and City != ""):
            Value = (RollNo, First_Name, Last_Name, Phone_Number, City)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
        else:
            if (First_Name == "" and Last_Name == "" and Phone_Number == "" and City == ""):
                if (First_Name == "" and Last_Name == "" and Phone_Number == "" and City == ""):
                    messagebox.askokcancel(
                        "Information", "New Entery Fill All Details")
                else:
                    messagebox.askokcancel(
                        "Information", "Some fields left blank")
            else:
                messagebox.askokcancel("Information", "Record Already exists")
'''


def Register():
    RollNo = e1.get()
    Select = "SELECT COUNT(*) FROM student WHERE RollNo = %s"
    mycursor.execute(Select, (RollNo,))
    result = mycursor.fetchone()
    dbRollNo = result[0] if result else 0
    if int(RollNo) != int(dbRollNo):
        Insert = "INSERT INTO student (RollNo, First_Name, Last_Name, Phone_Number, City) VALUES (%s, %s, %s, %s, %s)"
        First_Name = e2.get()
        Last_Name = e3.get()
        Phone_Number = e4.get()
        City = e5.get()
        if First_Name and Last_Name and Phone_Number and City:
            Value = (RollNo, First_Name, Last_Name, Phone_Number, City)
            try:
                mycursor.execute(Insert, Value)
                mydb.commit()
                messagebox.showinfo("Information", "Record inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error inserting record: {err}")
        else:
            messagebox.showinfo("Information", "Fill all details")
    else:
        messagebox.showinfo("Information", "Record already exists")
        button1 = Button(root, text="Register", width=10,
                         height=2, command=Register).grid(row=7, column=0)


root.mainloop()
