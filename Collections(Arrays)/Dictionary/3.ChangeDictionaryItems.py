# You can change the value of a specific item by referring to its key name
mydict={"brand":"Ford","model":["Mustang","Ferrari","Mazda"],"year":1964,"electric":False}
mydict["year"]=2023
print(mydict)

# The update() method will update the dictionary with the items from the given argument
# The argument must be a dictionary, or an iterable object with key:value pairs
mydict.update({"electric":True})
print(mydict)