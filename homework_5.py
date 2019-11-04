class Animal(object):
    def __init__(self, defend, attack, name):
        self.health = 100
        self.attack = attack
        self.name = name
        self.defend = defend


class Human(Animal):
    def is_dangerous(self, animal):
        pass


human = Human(100, 7, 'Hercules')
animal = Animal(100, 12, 'Scorpion')

print(human.name, human.health, human.attack)
print(animal.name, animal.health, animal.attack)