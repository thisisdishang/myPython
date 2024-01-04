# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name
mydict={"Name":"Barbie","Age":25,"Gender":"Female","DOB":"01/01/2023"}
mydict.pop("Age")
print(mydict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
mydict.popitem()
print(mydict)

# The del keyword removes the item with the specified key name
del mydict["Name"]
print(mydict)

# The del keyword can also delete the dictionary completely
del mydict
# print(mydict) #this will cause an error because "thisdict" no longer exists

# The clear() method empties the dictionary
mydict2={"name":"Jamon","Age":25}
print(mydict2)
mydict2.clear()
print(mydict2)