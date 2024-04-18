# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

import re

# The findall() Function:
# The findall() function returns a list containing all matches
txt="Now i become death the destroyer of the world"
x=re.findall("de",txt)
print(x)

# The list contains the matches in the order they are found
# If no matches are found, an empty list is returned
x=re.findall("jh",txt)
print(x)

# The search() Function:
# The search() function searches the string for a match, and returns a Match object if there is a match.\
# If there is more than one match, only the first occurrence of the match will be returned
s=re.search("\s",txt)
print("The first white-space character is located in position:",s.start())

# If no matches are found, the value None is returned
s=re.search("hello",txt)
print(s)

# The split() Function:
# The split() function returns a list where the string has been split at each match
sp=re.split("\s",txt)
print(sp)

# You can control the number of occurrences by specifying the maxsplit parameter
sp=re.split("\s",txt,3)
print(sp)

# The sub() Function:
# The sub() function replaces the matches with the text of your choice
su=re.sub("\s","@",txt)
print(su)

# You can control the number of replacements by specifying the count parameter
su=re.sub("\s","@",txt,3)
print(su)