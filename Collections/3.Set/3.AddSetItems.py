# Change Items:
# Once a set is created, you cannot change its items, but you can add new items

# To add one item to a set use the add() method
myset={"BCA","BCOM","BTech","Bsc"}
myset.add("BBA")
print(myset)

# To add items from another set into the current set, use the update() method
allcourse={"BCA","BBA","BCOM"}
masterset={"MCA","MBA","MCOM"}
allcourse.update(masterset)
print(allcourse)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
mylist=["Windows","MAC","Linux"]
myset={"OS","iOS","WebOS"}
myset.update(mylist)
print(myset)