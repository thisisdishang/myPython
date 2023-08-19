# Python has a set of built-in methods that you can use on strings
# All string methods return new values. They do not change the original string

# capitalize() method Converts the first character to upper case
x = "patel"
print(x.capitalize())

# casefold() method Converts string into lower case
x = "EVIL"
print(x.casefold())

# The center() method will center align the string, using a specified character (space is default) as the fill character
x = "Dishang"
print(x.center(10, "O"))

# count() method Returns the number of times a specified value occurs in a string
x = "madam"
print(x.count("m"))

# encode() method Returns an encoded version of the string
x = "Rana"
print(x.encode())

# startswith() method Returns true if the string starts with the specified value
x = "bruce"
print(x.startswith('e'))
print(x.startswith('b'))

# endswith() method Returns true if the string ends with the specified value
x = "bruce"
print(x.endswith('e'))
print(x.endswith('k'))

# expandtabs() method Sets the tab size of the string
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

# find() method Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("to")
print(x)

x = txt.find("m", 5, 15)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(txt.find("q"))
# print(txt.index("q"))

# index() method Searches the string for a specified value and returns the position of where it was found
x = "Rana Corpo"
print(x.index("o"))

# isalnum() method Returns True if all characters in the string are alphanumeric
x = "/*/-"
print(x.isalnum())
x = "ADhaj23"
print(x.isalnum())

# isalpha() method Returns True if all characters in the string are in the alphabet
x = "2121"
print(x.isalpha())
x = "aBC"
print(x.isalpha())

# isascii() method Returns True if all characters in the string are ascii characters
x = "£"
print(x.isascii())

x = "?"
print(x.isascii())

# isdecimal() method Returns True if all characters in the string are decimals
x = "9"
print(x.isdecimal())

# isdigit() method Returns True if all characters in the string are digits
x = "4"
print(x.isdigit())

x = "F"
print(x.isdigit())

# isidentifier() method Returns True if the string is an identifier
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# islower() method Returns True if all characters in the string are lower case
x = "hello"
print(x.islower())

x = "DIKU"
print(x.islower())

# isnumeric() method Returns True if all characters in the string are numeric
x = "786"
print(x.isnumeric())
x = "PKD"
print(x.isnumeric())

# isprintable() method Returns True if all characters in the string are printable
a = "RANA"
print(x.isprintable())

# isspace()	method Returns True if all characters in the string are whitespaces
x = "D"
print(x.isspace())

x = " "
print(x.isspace())

# istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False
x="Rana"
print(x.istitle())

x="rana"
print(x.istitle())

# isupper()	method Returns True if all characters in the string are upper case
x="RANA"
print(x.isupper())

x="rana"
print(x.isupper())

# join() method Joins the elements of an iterable to the end of the string
a=["Dishang","Rana"]
x="H".join(a)
print(x)

# ljust() method Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20, "O")
print(x)

# rjust() method Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20, "O")
print(x)

# maketrans() method Returns a translation table to be used in translations
# translate() method Returns a translated string
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(mytable)
print(txt.translate(mytable))

# partition() method Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# rpartition() method Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.rpartition("bananas")
print(x)

# rfind() method Searches the string for a specified value and returns the last position of where it was found
# rindex() method Searches the string for a specified value and returns the last position of where it was found
txt = "La casa,De casa."
x = txt.rfind("casa")
print(x)

x = txt.rindex("casa")
print(x)

# splitlines() method Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# swapcase() method Swaps cases, lower case becomes upper case and vice versa
x="Rana Corpo"
print(x.swapcase())

# title() method Converts the first character of each word to upper case
x="rana kumar"
print(x.title())

# zfill() method Fills the string with a specified number of 0 values at the beginning
x="Dishang"
print(x.zfill(10))

"""
Method	        Decription
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
upper()	        Converts a string into upper case
lower()	        Converts a string into lower case
strip()	        Returns a trimmed version of the string
lstrip()	    Returns a left trim version of the string
rstrip()	    Returns a right trim version of the string
replace()	    Returns a string where a specified value is replaced with a specified value
split()     	Splits the string at the specified separator, and returns a list
rsplit()	    Splits the string at the specified separator, and returns a list
"""