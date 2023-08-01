# Strings in python are surrounded by either single quotation marks, or double quotation marks

# 'hello' is the same as "hello"
print('Hello')
print("Hello")

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string
x="Rana"
print(x)

# You can assign a multiline string to a variable by using three quotes
# You can use three double quotes
y="""Hi there
i am dishang rana
the founder ."""
print(y)

# You can use three single quotes
y='''Hi there
i am dishang rana
the founder .'''
print(y)

# Note:the line breaks are inserted at the same position as in the code

# Strings are Arrays
# strings in Python are arrays of bytes representing unicode characters
# Python does not have a character data type, a single character is simply a string with a length of 1

# Square brackets can be used to access elements of the string
# Get the character at position 1 (remember that the first character has the position 0)
h="Rana Dishang"
print(h[5],"\n")


# Since strings are arrays, we can loop through the characters in a string, with a for loop
a="Shree Hari"
for i in a:
    print(i)

# The len() function returns the length of a string
# Count space also
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in
print("Shree" in a)
print("Ram" in a)

# Use it in an if statement
if "Hari" in a:
    print("Yes, 'Hari' is present.")
else:
    print("No, 'Hari' is not present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
print("Rama" not in a)

# Use not in in a if statement
if "Rama" not in a:
    print("No, 'Rama' is NOT present.")
