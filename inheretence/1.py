import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Msg(self):
        print("It's just a triangle")

    def Perimeter(self):
        return self.a + self.b + self.c
    
    def Area(self):
        p = self.Perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class EquiTriangle(Triangle):
    def __init__(self, a):
        self.a = a 

    def Msg(self):
        print("It's an equilateral triangle")

    def Perimeter(self):
        return self.a * 3

    def Area(self):
        return (math.pow(self.a, 2) * math.sqrt(3)) / 4

class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Msg(self):
        print("It's a right triangle")

    def Area(self):
        return (self.a * self.b) / 2

triangle = Triangle(2, 3, 4)
eTriangle = EquiTriangle(5)   
rTriangle = RightTriangle(6, 8, 10)

print("Triangle:")
triangle.Msg()
print(f"Perimeter: {triangle.Perimeter()}")
print(f"Area: {triangle.Area()}\n")

print("EquiTriangle:")
eTriangle.Msg()
print(f"Perimeter: {eTriangle.Perimeter()}")
print(f"Area: {eTriangle.Area()}\n")

print("RightTriangle:")
rTriangle.Msg()
print(f"Perimeter: {rTriangle.Perimeter()}")
print(f"Area: {rTriangle.Area()}\n")

print(isinstance(rTriangle, Triangle))
print(isinstance(eTriangle, Triangle))
