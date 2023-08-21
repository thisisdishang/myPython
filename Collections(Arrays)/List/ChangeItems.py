# List:
mylist=["Mouse","Keyboard","Pendrive","CD","Speaker","SSD"]
print(mylist)

# To change the value of a specific item, refer to the index number
mylist[3]="HDD"
print(mylist)

"""To change the value of items within a specific range, define a list with the new values,
and refer to the range of index numbers where you want to insert the new values"""
mylist[1:3]=["DVD","CD"]
print(mylist)

"""If you insert more items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly"""
mylist2=["Mouse","CD","Speaker"]
mylist2[1:2]=["Keyboard","Pendrive"]
print(mylist2)

mylist[4:5]=["Keyboard","Pendrive"]
print(mylist)
# Note:The length of the list will change when the number of items inserted does not match the number of items replaced

"""If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly"""
mylist3 = ["apple", "banana", "cherry"]
mylist3[1:3] = ["watermelon"]
print(mylist3)

# To insert a new list item, without replacing any of the existing values, we can use the insert() method
# The insert() method inserts an item at the specified index
mylist3.insert(2,"mango")
mylist3.insert(0,"cherry")
print(mylist3)