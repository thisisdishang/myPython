# Python code to find the factorial of a number
# Using while loop
def myfact1(num):
    fact=1
    i=1
    n=num
    
    while(n!=0):
        fact*=n
        n-=1
        
    print(f"Factorial of number {num} using while loop is {fact}")

# Using for loop
def myfact2(num):
    fact=1
    for i in range(1,num+1):
        fact*=i

    print(f"Factorial of number {num} using for loop is {fact}")

num=int(input("Enter the number:"))
myfact1(num)
myfact2(num)