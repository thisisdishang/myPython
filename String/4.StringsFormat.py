# As we learned in the Python we cannot combine strings and numbers But we can combine strings and numbers by using the format() method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age=21
w="I am Dishang, and My Age is {}"
print(w.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
dollar=1
rupees=82.84
s="{} dollar is equal to {} rupee"
print(s.format(dollar,rupees))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
s="{1} rupee is equal to {0} dollar"
# dollar is at 0 index
# ruppes is at 1 index
print(s.format(dollar,rupees))