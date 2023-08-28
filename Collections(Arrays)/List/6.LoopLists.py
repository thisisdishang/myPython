# You can loop through the list items by using a for loop
mylist=["Mouse","Keyboard","Pendrive","Speaker","SSD"]
for i in mylist:
    print(i)

# You can also loop through the list items by referring to their index number
# Use the range() and len() functions to create a suitable iterable
print("\nLength Of List:",len(mylist))
print("\nUsing for loop:-")
for i in range(len(mylist)):
    print(i,mylist[i])

# You can loop through the list items by using a while loop
"""Use the len() function to determine the length of the list, then start at 0 
and loop your way through the list items by referring to their indexes"""
# Remember to increase the index by 1 after each iteration
i=0
print("\nUsing while loop:-")
while i<len(mylist):
    print(mylist[i])
    i+=1

# List Comprehension offers the shortest syntax for looping through lists
print("\nList Comprehensionp:-")
[print(i) for i in mylist]