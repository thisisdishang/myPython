# To remove an item in a set, use the remove(), or the discard() method
myset={"MCA","BCA","BTech","MTech"}
myset.remove("MTech")
print(myset)

# Note: If the item to remove does not exist, remove() will raise an error
# myset.remove("MBA")

myset2={"OS","iOS","WebOS","ChromeOS"}
myset2.discard("WebOS")
print(myset2)

# Note: If the item to remove does not exist, discard() will NOT raise an error
myset2.discard("AndroidOS")
print(myset2)

"""You can also use the pop() method to remove an item, but this method will remove a random item, 
so you cannot be sure what item that gets removed"""
# The return value of the pop() method is the removed item
myset3={"A","B","C","D","E"}
myset3.pop()
print(myset3)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed

# The clear() method empties the set
myset3.clear()
print(myset3)

# The del keyword will delete the set completely
del myset3
# print(myset3)