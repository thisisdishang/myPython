import MyModule

# Note: When using a function from a module, use the syntax: module_name.function_name
MyModule.greeting("Lucy")

l=MyModule.person["name"]
print(l)

import MyModule as mm
mm.greeting("Karl")

from MyModule import person
print(person['country'])

# printing all variables and function names of the "MyModule" module
print(dir(MyModule))