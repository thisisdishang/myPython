# List items are indexed and you can access them by referring to the index number
# Note:The first item has index 0
list1=["Mouse","Keyboard","Pendrive"]
print(list1[2])

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc
print(list1[-2])

# You can specify a range of indexes by specifying where to start and where to end the range
# When specifying a range, the return value will be a new list with the specified items
# Note:The search will start at index 2 (included) and end at index 4 (not included)
list2=["Mouse","Keyboard","Pendrive","CD","Speaker","SSD"]
print(list2[2:4])

# By leaving out the start value, the range will start at the first item
print(list2[:4])

# By leaving out the end value, the range will go on to the end of the list
print(list2[3:])

# Specify negative indexes if you want to start the search from the end of the list
print(list2[-4:-1])

# To determine if a specified item is present in a list use the in keyword
if "SSD" in list2:
    print("Yes Present!")
else:
    print("Not Present!")