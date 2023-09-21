# You can access the items of a dictionary by referring to its key name, inside square brackets
mydict={"brand":"Ford","model":["Mustang","Ferrari","Mazda"],"year":1964,"electric":False}
print(mydict["model"])

# There is also a method called get() that will give you the same result
print(mydict.get("year"))

# The keys() method will return a list of all the keys in the dictionary
print(mydict.keys())

"""The list of the keys is a view of the dictionary, meaning that any changes done 
to the dictionary will be reflected in the keys list"""
# After the change
mydict["color"]=["Black","Red"]
print(mydict.keys())

# The values() method will return a list of all the values in the dictionary
print(mydict.values())

"""The list of the values is a view of the dictionary, meaning that any changes done 
to the dictionary will be reflected in the values list"""
# After the change
mydict["year"]=2003
print(mydict.values())

# Add a new item to the original dictionary, and see that the values list gets updated as well
# After the change
mydict["rating"]=5
print(mydict.values())

# The items() method will return each item in a dictionary, as tuples in a list
print(mydict.items())

"""The returned list is a view of the items of the dictionary, meaning that any changes done 
to the dictionary will be reflected in the items list"""
mydict["year"]=2023
print(mydict.items())

# Add a new item to the original dictionary, and see that the items list gets updated as well
# After the change
mydict["petrol"]="Yes"
print(mydict.items())

# To determine if a specified key is present in a dictionary use the in keyword
if "electric" in mydict:
    print("Yes it's present!")