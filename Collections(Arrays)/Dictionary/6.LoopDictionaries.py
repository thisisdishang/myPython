# You can loop through a dictionary by using a for loop
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
mydict={"Name":"Barbie","Age":21,"Gender":"Female"}

# Print all key names in the dictionary, one by one
for i in mydict:
    print(i)

# Print all values in the dictionary, one by one
for i in mydict:
    print(mydict[i])

mydict2={"Name":"Bruce","Age":45,"Gender":"Male"}
# You can also use the values() method to return values of a dictionary
for i in mydict2.values():
    print(i)

# You can use the keys() method to return the keys of a dictionary
for i in mydict2.keys():
    print(i)

# Loop through both keys and values, by using the items() method
for i in mydict.items():
    print(i)

for i in mydict2.items():
    print(i)