# A Match Object is an object containing information about the search and the result
# Note: If there is no match, the value None will be returned, instead of the Match Object
import re
txt="Now i become death the destroyer of the World"
x=re.search("de",txt)
print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Print the position (start- and end-position) of the first match occurrence
# The regular expression looks for any words that starts with an upper case "W":
s=re.search(r"\bW\w+",txt)
print(s.span())
print(s.string)
print(s.group())