# There are several ways to join two or more sets in Python
"""You can use the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another"""

myset1={"A","B","C"}
myset2={1,2,3}
myset3=myset1.union(myset2)
print(myset3)

myset1.update(myset2) # type: ignore
print(myset1)

# Note: Both union() and update() will exclude any duplicate items
a={1,2,3,4}
b={1,4,5}
a.update(b)
print(a)

# Keep only the Duplicates:
# The intersection_update() method will keep only the items that are present in both sets
x={"rana","patel","jariwala","panchal","makwana"}
y={"shah","patel","rana","rathod"}
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets
z=x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates:
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x={"ios","android","chromeos"}
y={"macos","ios","webos"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
x={"ios","android","chromeos"}
y={"macos","ios","webos"}
z=x.symmetric_difference(y)
print(z)