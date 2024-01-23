# Python Program to reverse a number and also find the Sum of digits in the reversed number. Prompt the user for input

n=int(input("Enter the number:"))
rev=sum=0
temp=n
while(temp!=0):
    digit=temp%10
    rev=rev*10+digit
    sum+=digit
    temp//=10

print(f"Reverse Number is {rev}")
print(f"Sum of Number is {sum}")