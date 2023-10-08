# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
"""This is less like the for keyword in other programming languages, and works more like an iterator method 
as found in other object-orientated programming languages"""
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

mylist=["Keyboard","Mouse","Speaker"]
for i in mylist:
    print(i)

# Note: The for loop does not require an indexing variable to set beforehand whereas in while loop it's required

# Looping Through a String:
# Even strings are iterable objects, they contain a sequence of characters
for i in "Jarvis":
    print(i)

# The range() Function:
# To loop through a set of code a specified number of times, we can use the range() function
"""The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number"""
for i in range(8):
    print(i)

"""The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter"""
for i in range(1,5):
    print(i)

"""The range() function defaults to increment the sequence by 1, however it is possible to specify the increment 
value by adding a third parameter"""
for i in range(1,8,2):
    print(i)

# Else in For Loop:
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for i in range(10,16):
    print(i)
else:
    print("loop finished...")

# Note: The else block will NOT be executed if the loop is stopped by a break statement
for i in range(10,16):
    if i==13:
        break
    print(i)
else:
    print("loop finished...")

# Nested Loops:
# A nested loop is a loop inside a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop"
color=["red","blue","green"]
alpha=["A","B","C"]
number=[1,2,3]
for a in color:
    for b in alpha:
        for c in number:
            print(a,b,c)