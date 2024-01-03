# Python program to design calculator
a=float(input("Enter The Number 1:"))
b=float(input("Enter The Number 2:"))

print("\nSimple Calculator:-")
print("\n1.Addition\n2.Substraction\n3.Division\n4.Multiplication\n5.Exit")
ch=int(input("\nEnter Your Choice:"))

if ch==1:
    print("\nAddition is: ",a+b)
elif ch==2:
    print("\nSubstraction is: ",a-b)
elif ch==3:
    if b==0 or a==0:
        print("\nYou can not take input as zero")
    else:
        print("\nDivision is: ",a/b)
elif ch==4:
    print("\nMultiplication is: ",a*b)
else:
    exit()