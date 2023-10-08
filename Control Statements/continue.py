# With the continue statement we can stop the current iteration, and continue with the next
a=0
while a<8:    
    a+=1
    if a==5:
        continue
    print(a) 

# With the continue statement we can stop the current iteration of the loop, and continue with the next
mylist=["Keyboard","Mouse","Speaker"]
for i in mylist:
    if i=="Mouse":
        continue
    print(i)