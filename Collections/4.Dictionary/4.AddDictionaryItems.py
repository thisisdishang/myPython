# Adding an item to the dictionary is done by using a new index key and assigning a value to it
cardict={"brand":"Ford","model":["Mustang","Ferrari","Mazda"],"year":1964,"electric":False}
cardict["color"]="navy blue"
print(cardict)

# The update() method will update the dictionary with the items from a given argument
# If the item does not exist, the item will be added
# The argument must be a dictionary, or an iterable object with key:value pairs
cardict.update({"price":"$1500000"})
print(cardict)