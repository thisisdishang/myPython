# Python program to perform a linear search for a given Key number in the list and report Success or Failure

def search(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1

mylist=[12,78,3,6,8,10]
print(mylist)

l=int(input("Enter the element to search: "))
res=search(mylist,l)

if res!=-1:
    print("Success")
    print(f"{l} found at index",res)
else:
    print("Fail")