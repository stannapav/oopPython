class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def About(self):
        pass

    def Sound(self):
        pass

    def Play(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, breed):
        super(Cat, self).__init__(name, age)
        self.breed = breed

    def About(self):
        print(f'Hi this is {self.breed} and their name is {self.name} and {self.age} years old')

    def Sound(self):
        print(f'{self.name} makes sound Meow')

    def Play(self):
        print(f'{self.name} played with cat toys')

class Dog(Animal):
    def __init__(self, name, age, size):
        super(Dog, self).__init__(name, age)
        self.size = size

    def About(self):
        print(f'Hi this is Dog and their name is {self.name} and {self.age} years old and their size is {self.size}')

    def Sound(self):
        print(f'{self.name} makes sound Woof')

    def Play(self):
        print(f'{self.name} played with cat toys')

def ShowOff(animal):
    animal.About()
    animal.Sound()
    animal.Play()

cat = Cat('Diand', 11, 'British')
dog = Dog('Justin', 1, 'small')

print('Cat:')
ShowOff(cat)

print('\nDog:')
ShowOff(dog)