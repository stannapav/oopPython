import datetime

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def About(self):
        print(f'Hi this is {self.breed} and their name is {self.name} and {self.age} years old')

    def Sound(self):
        print(f'{self.name} makes sound Meow')

    def __eq__(self, other):
        if self.breed == other.breed:
            return 'Same breeds'
        else:
            return 'Diff breeds'
        
    def __str__(self):
        return f'Hi this is {self.breed} and their name is {self.name} and {self.age} years old'
    
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
            return f'х = {self.x}, y = {self.y}'
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

today = datetime.datetime.now()
s = 'I love cats'
cat1 = Cat('Diana', 11, 'British')
cat2 = Cat('Anna', 18, 'Human')
cat3 = Cat('Maks', 4, 'British')
point1 = Point(2, 3)
point2 = Point(1, 5)

print('str:')
print(str(s))
print(str(2.0/11.0))
print(str(today))

print('\nrepr:')
print(repr(s))
print(repr(2.0/11.0))
print(repr(today))

print('\nOverload')
print(str(cat1))
print(cat1 == cat2)
print(cat1 == cat3)
print(str(point1))
print(f'sub :{point1 - point2}')
print(f'mul :{point1 * point2}')