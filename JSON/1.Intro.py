# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation
# Python has a built-in package called json, which can be used to work with JSON data

# Parse JSON - Convert from JSON to Python:
# If you have a JSON string, you can parse it by using the json.loads() method
import json

# some JSON:
myjson='{"name":"Lucy","age":45,"City":"Nowhere"}'

# parse myjson:
o=json.loads(myjson)

# the result is a python dictionary:
print(o)
print(o["name"])

# Convert from Python to JSON:
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method
# take a python dictionary object:
mydict={"name":"Elli","age":19,"City":"America"}

# convert into JSON:
y=json.dumps(mydict)

# the result is a JSON string:
print(y)

# We can convert Python objects of the following types, into JSON strings:
# dict, list, tuple, string, int, float, True, False, None
print(json.dumps({"name":"Jarvis","age":18}))
print(json.dumps(["Red","Blue"]))
print(json.dumps(("one","two","three")))
print(json.dumps("myworld"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(False))
print(json.dumps(True))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python	JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null

# Convert a python object containing all the legal data types:
x = {"name": "Jack",
     "age": 42,
     "married": True,
     "divorced": False,
     "children": ("Ann","Billy"),
     "pets": None,
     "cars": [
         {"model": "BMW 230", "mpg": 27.5},
         {"model": "Ford Edge", "mpg": 24.1}
         ]
     }
print(json.dumps(x))

# Format the Result:
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks
# The json.dumps() method has parameters to make it easier to read the result
# Use the indent parameter to define the numbers of indents
print(json.dumps(x,indent=4))

"""We can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object,
and a colon and a space to separate keys from values"""
# Use the separators parameter to change the default separator:
print(json.dumps(x,indent=3,separators=(". ","= ")))

# Order the Result:
# The json.dumps() method has parameters to order the keys in the result
# Use the sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x,indent=4,sort_keys=True))