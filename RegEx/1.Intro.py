# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
# RegEx can be used to check if a string contains the specified search pattern

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions
import re
txt="Now i become death the destroyer of the world"
'''Search the string to see if it starts with "Now" and ends with "world"'''
x=re.search("^Now.*world$",txt)
print(x)

# Metacharacters
# Metacharacters are characters with a special meaning:
# Character	Description	                Example	
# []	    A set of characters	        "[a-m]"	
# \	        Signals a special sequence  "\d"	
# .	        Any character               "he..o"	
# ^	        Starts with	                "^hello"	
# $	        Ends with	                "planet$"	
# *	        Zero or more occurrences	"he.*o"	
# +	        One or more occurrences	    "he.+o"	
# ?	        Zero or one occurrences	    "he.?o"	
# {}	    Exactly the specified number of occurrences	"he.{2}o"	
# |	        Either or	                "falls|stays"	
# ()	    Capture and group	 	 

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
# Character
# \A : Returns a match if the specified characters are at the beginning of the string example: "\AThe"	
# \b : Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the
#      string is being treated as a "raw string") example: r"\bain" r"ain\b"	
# \B : Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making
#      sure that the string is being treated as a "raw string") example: r"\Bain" r"ain\B"	
# \d : Returns a match where the string contains digits (numbers from 0-9) example: "\d"	
# \D : Returns a match where the string DOES NOT contain digits example: "\D"	
# \s : Returns a match where the string contains a white space character example: "\s"	
# \S : Returns a match where the string DOES NOT contain a white space character example: "\S"	
# \w : Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) example: "\w"	
# \W : Returns a match where the string DOES NOT contain any word characters example: "\W"	
# \Z : Returns a match if the specified characters are at the end of the string example: "Spain\Z"	

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set
# [arn] : Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	: Returns a match for any lower case character, alphabetically between a and n	
# [^arn] : Returns a match for any character EXCEPT a, r, and n	
# [0123] : Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9] : Returns a match for any digit between 0 and 9	
# [0-5][0-9] : Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z] : Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+] : In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string