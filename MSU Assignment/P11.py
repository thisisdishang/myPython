# Python program to check if a 3 digit number is Armstrong number or not

n=int(input("Enter the number:"))
sum=0
temp=n
while temp!=0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if sum==n:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")