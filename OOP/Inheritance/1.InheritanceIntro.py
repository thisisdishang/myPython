# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class
# Child class is the class that inherits from another class, also called derived class

# Create a parent class:
# Any class can be a parent class, so the syntax is the same as creating any other class
class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printdetails(self):
        print(self.name,self.age)

o1=father("Urus",47)
o1.printdetails()

# Create a child class:
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class son(father):
    pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class

o2=son("Kile",21)
o2.printdetails()

# Add init function child class:
# Note: The __init__() function is called automatically every time the class is being used to create a new object
# We want to add the __init__() function to the child class (instead of the pass keyword)
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class son2(father):
    def __init__(self, name, age):
        father.__init__(self,name,age)
    
# Here we kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function

# Use the super() function:
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
# Add properties & methods:
class son3(father):
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender=gender   

    def hello(self):
        print(f"{self.name} {self.age} {self.gender}")

y=son3("Urus",14,"Male")
y.hello()
