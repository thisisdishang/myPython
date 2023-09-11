# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unindexed
# Note: Set items are unchangeable, but you can remove items and add new items
# From Python's perspective, sets are defined as objects with the data type 'set'

# Sets are written with curly brackets
mysets={"A","B","C"}
print(type(mysets))
print(mysets)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear

# Set Items:
# Set items are unordered, unchangeable, and do not allow duplicate values

# Unordered:
# Unordered means that the items in a set do not have a defined order
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key

# Unchangeable:
# Set items are unchangeable, meaning that we cannot change the items after the set has been created
# Once a set is created, you cannot change its items, but you can remove items and add new items

# Duplicates Not Allowed:
# Sets cannot have two items with the same value
dupset={"PC",1,"PC",2,"PC",3,"PC",4}
print(dupset)

# Note: The values True 1 and False 0 are considered the same value in sets, and are treated as duplicates
# True==1 False==0
dupset2={1,True,"HELLO","People",False,0}
print(dupset2)

# Get the Length of a Set:
# To determine how many items a set has, use the len() function
print(len(dupset))
print(len(dupset2))

# Set Items - Data Types:
# Set items can be of any data type
intset={1,2,3,4,5}
strset={"A","B","C","D"}
boolset={True,False}

# A set can contain different data types
mixset={1,"BCA",True,0.6}

# The set() Constructor:
# It is also possible to use the set() constructor to make a set
setcons=set(("A",0,"B",1))
print(type(setcons))
print(setcons)