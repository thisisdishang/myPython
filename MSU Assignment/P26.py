# Python program to create union and intersection of sets

set1 = {'1', '5', '6', '7', '8'}
set2 = {'2', '4', '9', '8', '7'}

print("Union of sets:", set1 | set2)
print("Intersection of sets:", set1 & set2)

# another way
print("Union of sets:", set1.union(set2))
print("Intersection of sets:", set1.intersection(set2))