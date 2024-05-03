# The try block lets you test a block of code for errors
# The except block lets you handle the error
# The else block lets you execute code when there is no error
# The finally block lets you execute code, regardless of the result of the try- and except blocks

# Exception Handling:
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message
# These exceptions can be handled using the try statement
try:
    print(x)
except:
    print("An exception occured...x is not defined")

# Note: Since the try block raises an error, the except block will be executed. Without the try block, the program will crash and raise an error
# print(x)

# Many Exceptions:
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else:
# You can use the else keyword to define a block of code to be executed if no errors were raised
try:
    print("I am indestructible")
except:
    print("Somethingw went wrong")
else:
    print("Nothing went wrong")

# Finally:
# The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("An exception occured...x is not defined")
finally:
    print("The try...except is finished")

# finally can be useful to close objects and clean up resources
# The program can continue, without leaving the file object open
try:
  f = open("demo.txt")
  try:
    f.write("Destroyer of world")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# Raise an exception:
# As a Python developer you can choose to throw an exception if a condition occurs
# To throw (or raise) an exception, use the raise keyword
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# We can define what kind of error to raise, and the text to print to the user
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")