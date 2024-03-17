# Write a python program to create student registration form and collect the data provied by student in database.

import sqlite3
from tkinter import *

# Function to submit data to database

def submit():
    # Connect to the database
    conn = sqlite3.connect('student.db')
    c = conn.cursor()

    # Create table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    gender TEXT,
                    course TEXT
                )''')

    # Insert data into the table
    c.execute("INSERT INTO students (name, age, gender, course) VALUES (?, ?, ?, ?)",
              (name_entry.get(), age_entry.get(), gender_entry.get(), course_entry.get()))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Clear the entry fields after submission
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    course_entry.delete(0, END)

# Create tkinter window
root = Tk()
root.title("Student Registration Form")
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
age_label = Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
gender_label = Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5)
course_label = Label(root, text="Course:")
course_label.grid(row=3, column=0, padx=10, pady=5)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry = Entry(root, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=5)
gender_entry = Entry(root, width=30)
gender_entry.grid(row=2, column=1, padx=10, pady=5)
course_entry = Entry(root, width=30)
course_entry.grid(row=3, column=1, padx=10, pady=5)
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Start the GUI
root.mainloop()