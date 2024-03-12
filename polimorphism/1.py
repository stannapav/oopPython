import math

class Triangle:
    def __init__(self, a, b, c, lineWidth = 1.0, color = 'none'):
        self.a = a
        self.b = b
        self.c = c
        self.lineWidth = lineWidth
        self.color = color

    def Msg(self):
        print("It's just a triangle")

    def Perimeter(self):
        return self.a + self.b + self.c
    
    def Area(self):
        p = self.Perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def Draw(self):
        print('Trialnge is build')
    
    def LineWidth(self):
        print(f'Line width of this triangle {self.lineWidth}')

    def Fill(self):
        print(f"This triangle color is {self.color}")


class EquiTriangle(Triangle):
    def __init__(self, a, lineWidth = 1.0, color = 'none'):
        super(EquiTriangle, self).__init__(a, a, a, lineWidth, color)

    def Msg(self):
        print("It's an equilateral triangle")

    def Perimeter(self):
        return self.a * 3

    def Area(self):
        return (math.pow(self.a, 2) * math.sqrt(3)) / 4
    
    def Draw(self):
        print('EquiTriangle is build')
    
    def LineWidth(self):
        print(f'Line width of this EquiTriangle {self.lineWidth}')

    def Fill(self):
        print(f"This EquiTriangle color is {self.color}")

class RightTriangle(Triangle):
    def __init__(self, a, b, c, lineWidth = 1.0, color = 'none'):
        super(RightTriangle, self).__init__(a, b, c, lineWidth, color)

    def Msg(self):
        print("It's a right triangle")

    def Area(self):
        return (self.a * self.b) / 2
    
    def Draw(self):
        print('RightTrialnge is build')
    
    def LineWidth(self):
        print(f'Line width of this RightTriangle {self.lineWidth}')

    def Fill(self):
        print(f"This RightTriangle color is {self.color}")

triangles = [Triangle(2, 3, 4), EquiTriangle(5, 1.5, 'red'), RightTriangle(6, 8, 10, 0.5, 'green')]

for triangle in triangles:
    triangle.Draw()
    triangle.Msg()
    print(f"Perimeter: {triangle.Perimeter()}")
    print(f"Area: {triangle.Area()}")
    triangle.LineWidth()
    triangle.Fill()
    print()