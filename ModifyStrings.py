# Python has a set of built-in methods that you can use on strings

# Upper Case
g="i love you 3000"
print(g.upper())

# Lower case
a="DIKU"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this 
# The strip() method removes any whitespace from the beginning or the end
k=" Hello, People "
print(k.strip())

# Replace String
l="Anatony"
print(l.replace("n","s"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items
# The split() method splits the string into substrings if it finds instances of the separator
l="Dishang#Rana#India"
print(l.split('#'))
print(type(l.split('#')))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator
a="God "
b="Is "
c="Almighty"
print(a+b+c)

# To add a space between them, add a " "
a="Hello"
b="People"
print(a+" "+b)