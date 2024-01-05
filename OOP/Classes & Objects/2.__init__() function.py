# To understand the meaning of classes we have to understand the built-in __init__() function
# All classes have a function called __init__(), which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
class men:
    def __init__(self,name,age):
        self.name=name
        self.age=age

m1=men("John",25)

print(m1.name)
print(m1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.