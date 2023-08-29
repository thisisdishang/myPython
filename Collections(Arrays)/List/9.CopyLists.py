"""You cannot copy a list simply by typing list2 = list1, because list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2"""
listone=["Insta","Snap","Whatsapp"]
listtwo=listone
listone.insert(1,"FB")
print(listtwo)

# There are ways to make a copy, one way is to use the built-in List method copy()
list1=["CD","DVD","USB"]
list2=list1.copy()
list2.append("RAM")
print(list2)
print(list1)

# Another way to make a copy is to use the built-in method list()
list1=["Keyboard","CPU","Mouse"]
list2=list(list1)
list2.insert(3,"SSD")
print(list2)
print(list1)