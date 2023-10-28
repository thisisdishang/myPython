# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression
# The expression is executed and the result is returned
a=lambda k:k+10
print(a(4))

# Lambda functions can take any number of arguments
x=lambda a,b:a*b
print(x(4,5))

y=lambda p,q,r:p+q+r
print(y(12,23,45))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def myfun(n):
    return lambda x:x*n

# Use that function definition to make a function that always doubles the number you send in
doubler=myfun(2)
print(doubler(4))

# Or, use the same function definition to make a function that always triples the number you send in
tripler=myfun(3)
print(tripler(9))

# Note:Use lambda functions when an anonymous function is required for a short period of time