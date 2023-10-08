# With the break statement we can stop the loop even if the while condition is true
a=1
while a<=7:    
    if a==5:
        break
    print(a)
    a+=1

# With the break statement we can stop the loop before it has looped through all the items
mylist=["Keyboard","Mouse","Speaker"]
for i in mylist:
    print(i)
    if i=="Mouse":
        break

# Exit the loop when i is "Mouse", but this time the break comes before the print
for i in mylist:
    if i=="Mouse":
        break
    print(i)