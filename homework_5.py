class Animal(object):
    def __init__(self, attack, name):
        self.health = 100
        self.attack = attack
        self.name = name


class Human(Animal):
    def is_dangerous(self, animal):
        self.health = 100
        while human.health > 0:
            human.health -= animal.attack
            animal.health -= human.attack
        if animal.health > human.health:
            print(f'{animal.name} is dangerous')
        else:
            print(f'{animal.name} not dangerous')


human = Human(17, 'Hercules')
animal = Animal(9, 'Scorpion')
animal_1 = Animal(1, 'Squirrel')
animal_2 = Animal(2, 'Dog')
human.is_dangerous(animal)
human.is_dangerous(animal_1)
human.is_dangerous(animal_2)


class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.know_people = []

    def know(self, person):
        if person.name not in self.know_people:
            self.know_people.append(person.name)

    def is_know(self, person):
        if person.name in self.know_people:
            print('Они знакомы')
        else:
            print('Они не знакомы')


person_1 = Person(25, 'Oleg')
person_2 = Person(26, 'Sergey')
person_3 = Person(25, 'Andrew')
print(person_1.name, person_2.name, person_3.name)
person_1.know(person_2)
person_1.is_know(person_2)
person_1.is_know(person_3)


class Printer(object):
    def log(self, *values):
        print(values)


class FormattedPrinter(Printer):
    def log(self, *values):
        print('**********')
        print(values)
        print('**********')


values = Printer()
values.log('sss', 2, [1, 2, '45'])
values2 = FormattedPrinter()
values2.log('sss', 2, [1, 2, '45'])
