class Shape:
    def area(self):
        print("Area method of Shape class")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle:", area)


# Object Creation
c1 = Circle(7)
r1 = Rectangle(10, 5)
t1 = Triangle(8, 6)

# Calling area() method
c1.area()
r1.area()
t1.area()
