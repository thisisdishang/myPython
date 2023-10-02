"""You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2"""
# There are ways to make a copy, one way is to use the built-in Dictionary method copy()
cardict={"brand":"Ford","model":["Mustang","Ferrari","Mazda"],"year":1964,"electric":False}
cardict2=cardict.copy()
print(cardict2)

cardict2["color"]="navy blue"

# Another way to make a copy is to use the built-in function dict()
cardict3=dict(cardict2)
print(cardict3)