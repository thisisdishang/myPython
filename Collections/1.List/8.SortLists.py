# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# Sort the list alphabetically
namelist=["Devin","Lumin","Waskin","Azim","Pulo","Cembin"]
namelist.sort()
print(namelist)

# Sort the list numerically
numlist=[10,55,30,48,96,68]
numlist.sort()
print(numlist)

# To sort descending, use the keyword argument reverse = True
namelist.sort(reverse=True)
print(namelist)

numlist.sort(reverse=True)
print(numlist)

# You can also customize your own function by using the keyword argument key = function
# The function will return a number that will be used to sort the list (the lowest number first)
# Sort the list based on how close the number is to 50
def myfun(n):
  return abs(n - 50)

mylist =[85,45,20,5,36,65]
mylist.sort(key = myfun)
print(mylist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
namelist=["Devin","lumin","Waskin","azim","Pulo","cembin"]
namelist.sort()
print(namelist)

# Luckily we can use built-in functions as key functions when sorting a list
# So if you want a case-insensitive sort function, use str.lower as a key function
namelist.sort(key=str.lower)
print(namelist)

# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements
namelist=["Devin","Lumin","Waskin","Azim","Pulo","Cembin"]
namelist.reverse()
print(namelist)