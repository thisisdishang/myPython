"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround"""
# You can convert the tuple into a list, change the list, and convert the list back into a tuple
mytuple=("PC","Laptop","Watch")
print(mytuple)
x=list(mytuple)
x[1]="CPU"  # type: ignore
mytuple=tuple(x)
print(mytuple)

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple
"""1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list,
add your item(s), and convert it back into a tuple"""
mytuple=("PC","Laptop","Watch")
x=list(mytuple)
x.append("CD") # type: ignore
mytuple=tuple(x)
print(mytuple)

"""2. Add tuple to a tuple: You are allowed to add tuples to tuples, so if you want to add one item, (or many),
create a new tuple with the item(s), and add it to the existing tuple"""
a=("DVD",)
mytuple+=a
print(mytuple)

"""Note: When creating a tuple with only one item, remember to include a comma after the item,
otherwise it will not be identified as a tuple"""

# Note: You cannot remove items in a tuple
"""Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround
as we used for changing and adding tuple items"""
mytuple=("PC","Laptop","Watch","CD","DVD")
x=list(mytuple)
x.remove("Watch")
mytuple=tuple(x)
print(mytuple)

# The del keyword can delete the tuple completely
del mytuple
# print(mytuple) # this will raise an error because the tuple no longer exists