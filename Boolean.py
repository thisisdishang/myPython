# When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(15 > 9)
print(100==100)
print(10 == 9)
print(15 < 9)

# The bool() function allows you to evaluate any value, and give you True or False in return
# Evaluate a string and a number
print(bool("hi"))
print(bool(10))

# Evaluate two variables
a="its me"
b=15
print(bool(a))
print(bool(b))

# Note:Almost any value is evaluated to True if it has some sort of content

# Any string is True, except empty strings
print(bool(""))

# Any number is True, except 0
print(bool(0))

# Any list, tuple, set, and dictionary are True, except empty ones
a=[]
b=()
c={}
d=None
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))

"""In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0,
and the value None. And of course the value False evaluates to False"""

"""One more value, or object in this case, evaluates to False, and that is if you have an object
that is made from a class with a __len__ function that returns 0 or False"""
class cars():
    def __len__(self):
        return 0

bmw = cars()
print(bool(bmw))

# You can create functions that returns a Boolean Value
def body():
    return True

print(body())

# You can execute code based on the Boolean answer of a function
# Print "YES" if the function returns True, otherwise print "NO"
if body():
    print("YES")
else:
    print("NO")

"""Python also has many built-in functions that return a boolean value, like the isinstance() function,
which can be used to determine if an object is of a certain data type"""
x="Dishu"
print(isinstance(x,str))
print(isinstance(x,int))

y=10
print(isinstance(y,int))

z=True
print(isinstance(z,bool))

a=2.9
print(isinstance(a,float))