# Python program to merge two list into list of tuples

def mergeList(list1, list2):
    list3 = list(zip(list1, list2))
    return list3


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(mergeList(list1, list2))