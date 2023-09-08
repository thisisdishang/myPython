# You can access tuple items by referring to the index number, inside square brackets
mytuple=("PC","Laptop","Watch")
print(mytuple[1])

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
print(mytuple[-1])

# You can specify a range of indexes by specifying where to start and where to end the range
# When specifying a range, the return value will be a new tuple with the specified items
mytuple2=("Keyboard","CPU","USB","DVD","Keyboard","CD","LED","Keyboard")
print(mytuple2[2:5])

# By leaving out the start value, the range will start at the first item
print(mytuple2[:4])

# By leaving out the end value, the range will go on to the end of the list
print(mytuple2[3:])

# Specify negative indexes if you want to start the search from the end of the tuple
print(mytuple2[-4:-1])

# To determine if a specified item is present in a tuple use the in keyword
if "LCD" in mytuple2:
    print("Yes! It's present in tuple")
else:
    print("No! It's not present in tuple")