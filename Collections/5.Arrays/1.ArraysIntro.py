# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead
# Here we shows how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library

# What is an Array? 
# Arrays are used to store multiple values in one single variable
# An array is a special variable, which can hold more than one value at a time

# Create an array
color=["Red","Blue","Green","Yellow","Pink"]

# Access the elements of an array
x=color[2]
print(x)

# Modify the value of the first array
color[0]="Purple"
print(color[0])

# The length of an array
# Note: The length of an array is always one more than the highest array index
print(len(color))

# Looping array elements
for i in color:
    print(i)

# Adding array elements
color.append("Red")
print(color)

# Removing array elements
# Using pop() method:
# pop(1) remove element at position 1 from array
color.pop(1)
# pop() remove by default last element from array
color.pop() 
print(color)

# Using remove() method:
# remove() method specifically remove from the value not from the position
color.remove("Green")
print(color)
# Note: The list's remove() method only removes the first occurrence of the specified value

# copy() method:
color2=color.copy()
print(color2)

# clear() method:
# Remove all the elements from the list
color.clear()
print(color)

# count() method:
print(color2.count("Yellow"))

# extend() method:
color.extend(color2)
print(color)

# index() method:
print(color.index("Pink"))

# insert() method:
color.insert(2,"Red")
print(color)

# reverse() method:
car=["BMW","Audi","Mercedez"]
print(car.reverse())

# sort() method:
print(car.sort())