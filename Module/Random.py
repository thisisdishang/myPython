# python has a built-in module called random that can be used to make random numbers
import random

print(random.randrange(1,9))

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
x=range(1,11,2)
for i in x:
    print(i)