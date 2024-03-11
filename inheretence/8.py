class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def About(self):
        print(f'Hi this is some animal and their name is {self.name} and {self.age} years old')

    def Sound(self, sound):
        print(f'{self.name} makes sound {sound}')

class Cat(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def About(self):
        print(f'Hi this is {self.breed} and their name is {self.name} and {self.age} years old')

    def Sound(self):
        print(f'{self.name} makes sound Meow')

class Dog(Animal):
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size

    def About(self):
        print(f'Hi this is Dog and their name is {self.name} and {self.age} years old and their size is {self.size}')

    def Sound(self):
        print(f'{self.name} makes sound Woof')
    
animal = Animal('Anna', 18)
cat = Cat('Diand', 11, 'British')
dog = Dog('Justin', 1, 'small')

print('Animal:')
animal.About()
animal.Sound('AAAAAAAAAAAAAA')

print('\nCat:')
cat.About()
cat.Sound()

print('\nDog:')
dog.About()
dog.Sound()