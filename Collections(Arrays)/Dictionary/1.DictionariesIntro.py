# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates

# Dictionaries are written with curly brackets, and have keys and values
mydict={"Name":"Barbie","Age":25,"Gender":"Female"}
print(mydict)

# From Python's perspective, Dictionary are defined as objects with the data type 'dict'
print(type(mydict))

# Dictionary Items:
# Dictionary items are ordered, changeable, and does not allow duplicates
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name
print(mydict["Name"])

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index

# Changeable:
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created

# Duplicates Not Allowed:
# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
mydict={"Name":"Barbie","Age":25,"Gender":"Female","Age":20}
print(mydict)

# Dictionary Length:
# To determine how many items a dictionary has, use the len() function
mydict2={"brand":"Ford","model":"Mustang","year":1964}
print(len(mydict2))

# Dictionary Items - Data Types:
# The values in dictionary items can be of any data type
# String, int, boolean, and list data types
mixdict={"brand":"Ford","model":["Mustang","Ferrari","Mazda"],"year":1964,"electric":False}
print(mixdict)

# The dict() Constructor:
# It is also possible to use the dict() constructor to make a dictionary
makedict=dict(name="James",age=35,gender="Male")
print(makedict)