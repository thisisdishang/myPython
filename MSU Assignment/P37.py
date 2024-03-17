# Write a python class named circle constructed by a radius and two methods which will compute area and perimeter

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())