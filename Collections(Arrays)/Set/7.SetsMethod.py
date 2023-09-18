# Python has a set of built-in methods that you can use on sets
# Method	                        Description
# add()	                            Adds an element to the set
# clear()	                        Removes all the elements from the set
# discard()	                        Remove the specified item
# intersection()	                Returns a set, that is the intersection of two other sets
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# pop()	                            Removes an element from the set
# remove()	                        Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                        Update the set with the union of this set and others

# copy():                        
# Returns a copy of the set
x={"1","A","2","B","3","C"}
y=x.copy()
print(y)

# difference():                    
# Returns a set containing the difference between two or more sets
x={"rana","patel","jariwala","panchal","makwana"}
y={"shah","patel","rana","rathod"}

# Return a set that contains the items that only exist in set x, and not in set y
z=x.difference(y)
print(z)

# Return a set that contains the items that only exist in set y, and not in set x
z=y.difference(x)
print(z)

# difference_update():	            
# Removes the items in this set that are also included in another, specified set
x.difference_update(y)
print(x)

# isdisjoint():	                    
# Returns whether two sets have a intersection or not
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False
x={"rana","patel","jariwala","panchal","makwana"}
y={"shah","patel","rana","rathod"}
z=x.isdisjoint(y)
print(z)

# issubset()	                    
# Returns whether another set contains this set or not
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False
x={"a","b","c"}
y={"d","e","f","g","a","b","c"}
z=x.issubset(y)
print(z)

# issuperset()	                    
# Returns whether this set contains another set or not
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)