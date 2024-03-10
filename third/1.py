class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def reflect_x(self):
        return {self.x, -self.y}
    
    def slope_from_origin(self):
        return self.y / self.x
    
    def getLine(self, otherPoint):
        x1 = otherPoint.x - self.x
        y1 = otherPoint.y - self.y
        k = y1 / x1
        b = (-self.x * y1 + -(-self.y * x1)) / x1

        return f'Рівняння прямої між двума ціма точками: у = {k} * x + {b}'
    
    def description(self):
        print(f'х = {self.x}, y = {self.y}')

    def reflect_y(self):
        return {-self.x, self.y}
    
    def reflect_xy(self):
        return {-self.x, -self.y}
    

p1 = Point(4, 11)
p2 = Point(6, 15)

print(f'reflect x {p1.reflect_x()}')
print(f'slope from origin {p1.slope_from_origin()}')
print(p1.getLine(p2))
print(f'reflect y {p1.reflect_y()}')
print(f'reflect xy {p1.reflect_xy()}')