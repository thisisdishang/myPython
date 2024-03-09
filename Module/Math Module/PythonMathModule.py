"""Python has a set of built-in math functions, including an extensive math module,
that allows you to perform mathematical tasks on numbers"""

# Built-in Math Functions
a=max(10,56,4,96) # find highest value
b=min(6,8,2,4) # find lowest value
q=abs(-5.25) # find absolute(positive) value
p=pow(2,3) # power of value

print(a)
print(b)
print(q)
print(p)

# Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions
# When you have imported the math module, you can start using methods and constants of the module
import math
print(math.sqrt(225)) # square root of a number
print(math.ceil(4.2)) # method rounds a number upwards to its nearest integer
print(math.floor(4.4)) # method rounds a number downwards to its nearest integer
print(math.pi)