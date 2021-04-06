import math

class Shape:
    def area(self):
        return 0

#   Rectangle is the subclass
#   Shape is the superclass
#   Rectangle inherits from Shape
class Rectangle(Shape):
    # Constructor -- when I make a Rectangle, this is the method that is called
    # Here we set default values or use parameters
    # self indicates that it pertains to a class
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def area(self):
        return self.w * self.l

    def toString(self):
        return f"width: {self.w}, length {self.l}, area {self.area()}"

class Square(Rectangle):
    def __init__(self, w):
        #Use the Rectangle constructor with width w as the argument for width and length of a Rectangle
        super().__init__(w, w)

    def toString(self):
        # return f"side: {self.w}, area {self.area()}"
        return "Square: " + super().toString()

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r**2)

    def toString(self):
        return f"radius {self.r}, area {self.area()}"


r1 = Rectangle(5, 4)
r2 = Rectangle(3, 6)
print(r1.toString())

c1 = Circle(1)
print(c1.toString())

s1 = Square(5)
print(s1.toString())
