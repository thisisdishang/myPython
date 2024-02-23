'''The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
with the same name that can be executed on many objects or classes'''

# Function polymorphism:
# An example of a Python function that can be used on different objects is the len() function
# On String
mystring = "I'm Indestructible"
print(len(mystring))

# On Tuple
mytuple = ("A", "B", "C", "D")
print(len(mytuple))

# On Dictionary
mydict = {"name": "bryer", "gender": "female"}
print(len(mydict))

# Class polymorphism:
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name
class bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print("Bike is running")


class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print("Car is running")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print("Plane is flying")


b1 = bike('Honda', 'Hornet')
c1 = car('BMW', 'X4')
p1 = plane('Boine', '456')

for i in (b1, c1, p1):
    i.run()

# Inheritance Class Polymorphism:
# We use polymorphism when classes with child classes with the same name
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print("Vehicle Run")


class car2(Vehicle):
    pass


class bike2(Vehicle):
    def run(self):
        print('Bike run')


class plane2(Vehicle):
    def run(self):
        print("Fly")


c2 = car2('Mercedes Benz', 'G Wagon')
b2 = bike2('Honda', 'Hornet')
p2 = plane2('Boein', '456')

for i in (c2, b2, p2):
    print(i.brand)
    print(i.model)
    i.run()

# Note: Child classes inherits the properties and methods from the parent class
# Because of polymorphism we can execute the same method for all classes