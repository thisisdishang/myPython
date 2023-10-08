# Python has two primitive loop commands:
# while loops
# for loops

# With the while loop we can execute a set of statements as long as a condition is true
a=1
while a<=7:
    print(a)
    a+=1

# Note: remember to increment variable, or else the loop will continue forever

# With the else statement we can run a block of code once when the condition no longer is true
a=1
while a<6:
    print(a)
    a+=1
else:
    print("a is no longer less than or equal 7")