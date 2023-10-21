# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# A function can return data as a result

# In Python a function is defined using the def keyword
def display():
    print("This is Display Function...")

# To call a function, use the function name followed by parenthesis
display()

# Arguments:
# Note: Arguments are often shortened to args in Python documentations
# Information can be passed into functions as arguments
"""Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma"""
def greeting(name):
    print("Hello "+name)

greeting("Hanon")
greeting("Twista")

# Number of Arguments:
"""By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, 
you have to call the function with 2 arguments, not more, and not less"""

# This function expects 2 arguments, and gets 2 arguments
def fullname(name,surname):
    print("Your Name is "+name)
    print("Your Surname is "+surname)

fullname("James","Parker")

# Note: If you try to call the function with 1 or 3 arguments, you will get an error

# Arbitrary Arguments, *args
# Note: Arbitrary Arguments are often shortened to *args in Python documentations
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition
# This way the function will receive a tuple of arguments, and can access the items accordingly
def namelist(*name):
    print("Good Morning "+name[2])

namelist("Harry","Rown","Karl","Peter")

# Keyword Arguments:
# Note: The phrase Keyword Arguments are often shortened to kwargs in Python documentations
# You can also send arguments with the key = value syntax
# This way the order of the arguments does not matter
def mynumbers(child1,child2,child3):
    print(child3+" is younger")

mynumbers(child1="Larn",child3="Karl",child2="Leo")

# Arbitrary Keyword Arguments, **kwargs
# Note: Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations
"""If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition"""
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def midname(**kwargs):
    print("His/Her middle name is "+kwargs["mname"])

midname(fname="James",mname="John",lname="Bond")

# Default Parameter Value:
# If we call the function without argument, it uses the default value
def mycountry(Country="India"):
    print("I am from "+Country)

mycountry("England")
mycountry()

# Passing a List as an Argument:
"""You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function"""
# E.g. if you send a List as an argument, it will still be a List when it reaches the function
color1=["Red","Green","Orange"]
color2=["Pink","Yellow","Blue"]
def mycolor(list1):
    for i in list1:
        print(i)

mycolor(color1)
mycolor(color2)

# Return Values:
# To let a function return a value, use the return statement
def sum(x,y):
    return x+y

print("Sum of two numbers:",sum(3,4))