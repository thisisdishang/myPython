# Lists are used to store multiple items in a single variable
"""Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage"""

# Lists are created using square brackets
mylist=["Keyboard","Mouse","Speaker"]
print(mylist)

# From Python's perspective, lists are defined as objects with the data type 'list'
print(type(mylist))

# List Items:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered:
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change
# If you add new items to a list, the new items will be placed at the end of the list
# Note:There are some list methods that will change the order, but in general the order of the items will not change

# Changeable:
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created

# Allow Duplicates:
# Since lists are indexed, lists can have items with the same value
duplicate=["Keyboard","Keyboard","Keyboard"]
print(duplicate)

# List Length:
# To determine how many items a list has, use the len() function
print(len(mylist))

# List Items - Data Types:
# List items can be of any data type
stringlist=["Dishang","Rana","Founder"]
intlist=[8586,8784,5296]
boollist=["True","False"]

# A list can contain different data types
mixlist=["Dishang",7,True]

# The list() Constructor:
# It is also possible to use the list() constructor when creating a new list
makelist=list(("Mango","Apple","Banana"))
print(makelist)

# count() method
mylist=["Keyboard","CPU","USB","DVD","Keyboard","CD","LED","Keyboard"]
print(mylist.count("Keyboard"))

# index() method
# Note: The index() method only returns the first occurrence of the value
print(mylist.index("CD"))