# Objects can also contain methods, Methods in objects are functions that belong to the object
class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Good to see you "+self.name)


o1 = myclass('Genesis', 19)
o1.greeting()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class

# The Self Parameter:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class myclass2:
    def __init__(my, name, age):
        my.name = name
        my.age = age

    def greeting(me):
        print("Good to see you "+me.name)


o2 = myclass2('Namesis', 24)
o2.greeting()

# Modify object properties
o1.name="Jarvis"
o2.name="Raone"
o1.greeting()
o2.greeting()

# Delete object properties
del o2.age
# print(o2.age) # o2 is not defined

# Delete objects
del o2
# print(o2) # o2 is not defined