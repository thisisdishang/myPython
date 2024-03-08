# Module
# Consider a module to be the same as a code library
# A file containing a set of functions you want to include in your application

# Create a Module
# To create a module just save the code you want in a file with the file extension .py
# Check MyModule.py file

# Use a Module
# Now we can use the module we just created, by using the import statement
# Check UseModule.py file

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
# Check MyModule.py file

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword
# Check UseModule.py file

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like
import platform
x=platform.python_version()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
# Note: The dir() function can be used on all modules, also the ones you create yourself
x=dir(platform)
print(x)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword
# Check UseModule.py file
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module