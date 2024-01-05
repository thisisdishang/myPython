# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned

# The string representation of an object without the __str__() function:
class men:
    def __init__(self,name,age):
        self.name=name
        self.age=age

m1=men("Karl",25)
print(m1)

# The string representation of an object with the __str__() function:
class men2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"

m1=men2("Otis",20)
print(m1)