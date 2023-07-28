# Variables that are created outside of a function are known as global variables
# Global variables can be used by everyone, both inside of functions and outside
a="Best"

def myfun():
    print("I Am "+a)

myfun()

"""If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value."""
a="Best"

def myfun():
    a="Good"
    print("I Am "+a)

myfun()

print("I Am "+a)

# To create a global variable inside a function, you can use the global keyword
def myfunc():
    global x
    x="Rana"


myfunc()
print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword
a="Best"

def myfun():
    global a
    a="Good"

myfun()
print("I Am "+a)