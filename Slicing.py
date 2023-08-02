# You can return a range of characters by using the slice syntax
# Specify the start index and the end index, separated by a colon, to return a part of the string
# first character has index 0
# last position not included

f="Rana Dishang"
print(f[1:7])

# By leaving out the start index, the range will start at the first character
print(f[:6])

# By leaving out the end index, the range will go to the end
print(f[2:])

# Use negative indexes to start the slice from the end of the string
# start with -1 index
print(f[-5:-3])