def revNum(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    print("Reverse Number is:",rev)

def paliNum(n):
    temp=n
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10

    if rev==temp:
        print(temp,"is palindrome number")
    else:
        print(temp,"is not palindrome number")

def armNum(n):
    temp=n
    sum=0
    while n!=0:
        digit=n%10
        sum+=digit**3
        n//=10

    if sum==temp:
        print(temp,"is armstrong number")
    else:
        print(temp,"is not armstrong number")
