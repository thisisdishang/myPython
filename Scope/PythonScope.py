# A variable is only available from inside the region it is created. This is called scope

# Local Scope:
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function
def locscope():
    k = 143
    print(k)

locscope()

# Function Inside Function:
def funinfun():
    k = 607

    def innerfun():
        print(k)
    innerfun()

funinfun()

# Global Scope:
# A variable created in the main body of the Python code is a global variable and belongs to the global scope
# Global variables are available from within any scope, global and local
g = 7
def func():
    print(g)

func()
print(g)

# Naming Variables:
'''If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
one available in the global scope (outside the function) and one available in the local scope (inside the function)'''
q = 5
def myfunc():
    q = 3
    print(q)

print(q)
myfunc()

# Global Keyword:
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword
# The global keyword makes the variable global
def j():
    global o
    o = 6

j()
print(o)

# use the global keyword if you want to make a change to a global variable inside a function
l = 87
def me():
    global l
    l = 86
    print(l)

me()
print(l)