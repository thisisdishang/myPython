# You can loop through the tuple items by using a for loop
mytuple=("Hi","Hello","What","How","Why","Yes","No","We")
for i in mytuple:
    print(i)

# You can also loop through the tuple items by referring to their index number
# Use the range() and len() functions to create a suitable iterable
mytuple=("Rana","Patel","Jariwala","Rathod")
for i in range(len(mytuple)):
    print(mytuple[i])

# You can loop through the tuple items by using a while loop
""" Use the len() function to determine the length of the tuple, then start at 0 and
loop your way through the tuple items by referring to their indexes"""
# Remember to increase the index by 1 after each iteration
mytuple=("CPU","RAM","ROM","USB")
i=0
while i<len(mytuple):
    print(i,mytuple[i])
    i+=1