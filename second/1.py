class Pet:
    species = 'animal'

    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age
        self.full = False
        self.playful = 0

    def about(self):
        return f"This is {self.name} and it's {self.animal} and {self.age} years old"
    
    def feed(self):
        if not self.full:
            self.full = True
            print(f'you feed your pet {self.name}')
        else:
            print(f'{self.name} is already full')

    def play(self):
        if self.playful == 0:
            self.playful = 1
            print(f'you played with your pet {self.name}')
        elif self.playful == 1:
            print(f'you played with your pet {self.name} but now they tired')
            self.playful = 2
        else:
            print(f'{self.name} is tired and do not want to play with you')
            
    
def getOlderPet(*pets):
    olderPet = pets[0]
    for pet in pets:
        if pet.age > olderPet.age:
            olderPet = pet

    return olderPet


def isAnimal(pet):
    if pet.species == 'animal':
        return True
    
    return False

cat1 = Pet('Cat', 'Diana', 11)
dog1 = Pet('Dog', 'Andy', 6)
dog2 = Pet('Dog', 'Justin', 1)
cat2 = Pet('Cat', 'Tea', 3)
lizard = Pet('Lizard', 'Cheese', 5)

olderPet = getOlderPet(cat1, cat2, dog1, dog2, lizard)
print(f'oldest pet: {olderPet.about()}')

print(f'Cat1 is animal {isAnimal(cat1)}')

cat1.feed()
cat1.feed()
cat1.play()
cat1.play()
cat1.play()
