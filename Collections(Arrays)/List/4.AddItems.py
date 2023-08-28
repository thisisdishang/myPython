# To add an item to the end of the list, use the append() method
mylist=["Mouse","Keyboard","Pendrive","CD","Speaker","SSD"]
mylist.append("ROM")
print(mylist)

# To append elements from another list to the current list, use the extend() method
# The elements will be added to the end of the list
mylist1=["Mouse","CD","Speaker"]
mylist2=["Keyboard","Pendrive"]
mylist1.extend(mylist2)
print(mylist1)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
mylist1=["SSD","HDD","DVD"]
print(type(mylist1))

mylist2=("Keyboard","Pendrive")
print(type(mylist2))

mylist3={"Name":"Dishang","Roll No":7}
print(type(mylist3))

mylist1.extend(mylist2)
print(mylist1)

mylist1.extend(mylist3)
print(mylist1)