# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets
# From Python's perspective, tuples are defined as objects with the data type 'tuple'

mytuple=("PC","Laptop","Watch")
print(type(mytuple))
print(mytuple)

# Tuple Items:
# Tuple items are ordered, unchangeable, and allow duplicate values
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc

# Ordered:
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change

# Unchangeable:
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow Duplicates:
# Since tuples are indexed, they can have items with the same value
duplicate=("PC","PC","PC")
print(duplicate)

# Tuple Length:
# To determine how many items a tuple has, use the len() function:
print(len(mytuple))

# Create Tuple With One Item:
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
onetuple=("Hello",)
print(type(onetuple))

# Not a tuple
onetuple=("Hello")
print(type(onetuple))

# Tuple Items - Data Types:
# Tuple items can be of any data type
stringtuple=("Dishang","Rana","Founder")
inttuple=(8586,8784,5296)
booltuple=("True","False")

# A tuple can contain different data types
mixtuple=("Dishang",7,True)

# The tuple() Constructor:
# It is also possible to use the tuple() constructor to make a tuple
mytuple2=tuple(("A","B","C"))
print(mytuple2)
print(type(mytuple2))