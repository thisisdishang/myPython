# An iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

# Iterator vs Iterable:
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from
# All these objects have a iter() method which is used to get an iterator
from traceback import print_tb


mylist=["apple","banana","cherry"]
myit=iter(mylist)

print(myit)
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters
mystring="gemini"
myit2=iter(mystring)
print(next(myit2))

# Looping through an iterator:
# Note: The for loop actually creates an iterator object and executes the next() method for each loop
for i in mylist:
    print(i)

for x in mystring:
    print(x)

# Create an Iterator:
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself
# The __next__() method also allows you to do operations, and must return the next item in the sequence
class NumGen:
    def __iter__(self):
        self.a=10
        return self
    
    def __next__(self):
        x=self.a
        self.a+=10
        return x
    
ob1=NumGen()
myiter=iter(ob1)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration:
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop
# To prevent the iteration from going on forever, we can use the StopIteration statement
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
class MyNum:
    def __iter__(self):
        self.x=1
        return self
    
    def __next__(self):
        if self.x<=10:
            y=self.x
            self.x+=1
            return y
        else:
            raise StopIteration
        
myob=MyNum()
myit3=iter(myob)

for i in myit3:
    print(i)