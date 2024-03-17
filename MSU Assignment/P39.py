'''create an abstract class shape and derive rectangle and circle from shape class. Implement abstract method of shape class in
rectangle and  circle class. Shape class contains: origin (x,y) as data member Display() and area() as abstract methods.
Circle contains : radious, Rectangle contains : length & width ( user inheritance , overloading  and overriding concept.)'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def Display(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def Display(self):
        print(
            f"Rectangle with origin ({self.x}, {self.y}), length {self.length}, width {self.width}")

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def Display(self):
        print(f"Circle with origin ({self.x}, {self.y}), radius {self.radius}")

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
rectangle = Rectangle(0, 0, 5, 4)
rectangle.Display()
print("Area of Rectangle:", rectangle.area())

circle = Circle(0, 0, 3)
circle.Display()
print("Area of Circle:", circle.area())