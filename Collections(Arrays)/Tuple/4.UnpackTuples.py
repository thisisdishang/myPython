# When we create a tuple, we normally assign values to it. This is called "packing" a tuple

# packing a tuple:
mytuple=("Hi","Hello","What")

# In Python, we are also allowed to extract the values back into variables. This is called "unpacking"

# unpacking a tuple:
(a,b,c)=mytuple
print(a)
print(b)
print(c)

"""Note: The number of variables must match the number of values in the tuple, if not,
you must use an asterisk to collect the remaining values as a list"""

"""If the number of variables is less than the number of values, you can add an * to the variable name
and the values will be assigned to the variable as a list"""
mytuple2=("Hi","Hello","What","How","Why")
(a,b,*c)=mytuple2
print(a)
print(b)
print(type(c))
print(c)

"""If the asterisk is added to another variable name than the last, Python will assign values to the variable
until the number of values left matches the number of variables left"""
mytuple3=("Hi","Hello","What","How","Why","Yes","No","We")
(a,*b,c,d)=mytuple3
print(a)
print(b)
print(c)
print(d)