# Python has no command for declaring a variable
# Variables are containers for storing data values.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x=2
y="Dishang"
print(x,"\n")
print(y)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
print(x)
y = int(3)    # y will be 3
print(y)
z = float(3)  # z will be 3.0
print(z)

# You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))
print(type(z))

# String variables can be declared either by using single or double quotes:
a='Dishang'
b="Rana"

# Variable names are case-sensitive
a="a"
A=45

# Assign Multiple Values
# Many Values To Multiple Variables
x,y,z="Dishang","Rana","07"
print(x)
print(y)
print(z)

# One Value To Multiple Variables
x=y=z="Khaer"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
colors=["Red","Blue","Green"]
a,b,c=colors
print(a)
print(b)
print(c)

# You output multiple variables, separated by a comma
p="I"
q="Am"
r="Indestructible"
s=3
print(p,q,r,s)

# You can also use the + operator to output multiple variables
# Space are excluded in + operator
print(p+q+r)

# Note:when you try to combine a string and a number with the + operator, Python will give you an error
# the + character works as a mathematical operator
a=10
b=2
print(a+b)
