# Python also accepts function recursion, which means a defined function can call itself
"""Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result."""
"""The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming"""
"""In this example, myrecursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0)."""
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it
def myrecursion(n):
    if(n>0):
        result=n+myrecursion(n-1)
        print(result)
    else:
        result=0
    return result

print("Recursion Example Results:-")
myrecursion(5)

# Fibonacci Program Using Recursion:
def Fibonacci(n): 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print("\nFibonacci Series:-") 
print(Fibonacci(6))