# Print all the pelindrom numbers in a list

mylist=[1331,25,262,123,90]
plist=[]

for i in mylist:
    rev=0
    temp=i
    while(temp!=0):
        digit=temp%10
        rev=rev*10+digit
        temp//=10

    if rev==i:
        plist.append(i)

print(mylist)
print(plist)