import math

# Base class: Shape
class Shape:
    def area(self):
        #This method should be overridden by derived classes.
        raise NotImplementedError("The area() method must be implemented by a subclass")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        #Initializes a rectangle with length and width.
        self.length = length
        self.width = width

    def area(self):
        #Calculates and returns the area of the rectangle.
        return self.length * self.width

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        #Initializes a circle with a radius.
        self.radius = radius

    def area(self):
        #Calculates and returns the area of the circle.
        return math.pi * (self.radius ** 2)

