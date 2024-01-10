# Python program to find particular character form given string and create new list for the index of that character

s=input("Enter the string: ")
find=input("Enter the character to search: ")
indexlist=[]
if find in s:
    print(f"Character found at {s.index(find)} in string")
    indexlist.append(s.index(find))
    print(indexlist)
else:
    print("Character not found in string")