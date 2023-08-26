# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

# Without list comprehension you will have to write a for statement with a conditional test inside
mylist=["Mouse","Keyboard","Pendrive","Speaker","SSD"]
newlist=[]

for i in mylist:
    if "S" in i:
        newlist.append(i)

print("Without List Comprehension:-\n",newlist)

# With list comprehension you can do all that with only one line of code
newlist=[i for i in mylist if "P" in i]
print("With List Comprehension:-\n",newlist)