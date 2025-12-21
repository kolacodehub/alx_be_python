import math


class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        return result
    
class Circle(Shape):
    def __init__(self, radius):
        # super().init()
        self.radius = radius

    def area(self):
        result = math.pi * (self.radius** 2)
        return result