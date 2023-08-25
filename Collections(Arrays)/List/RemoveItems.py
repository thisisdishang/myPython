# The remove() method removes the specified item
mylist1=["Mouse","Keyboard","Pendrive","CD","Speaker","SSD"]
mylist1.remove("CD")
print(mylist1)

# The pop() method removes the specified index
mylist2=["Mouse","Keyboard","Pendrive","Speaker","SSD"]
mylist2.pop(2)
print(mylist2)

# If you do not specify the index, the pop() method removes the last item
mylist2.pop()
print(mylist2)

# The del keyword also removes the specified index
mylist1=["Mouse","Keyboard","Pendrive","CD","Speaker","SSD"]
del mylist1[4]
print(mylist1)

# The del keyword can also delete the list completely
del mylist1
# print(mylist1) give error of not defined list

# The clear() method empties the list
# The list still remains, but it has no content otherhand del keyword completely delete the list
mylist2=["Mouse","Keyboard","Pendrive","Speaker","SSD"]
mylist2.clear()
print(mylist2)
print(type(mylist2))