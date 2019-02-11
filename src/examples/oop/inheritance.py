class Animal:
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

    def speak(self):
        print('I have no specific sound')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def speak(self):
        print('WOOF!')


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cat created')

    def speak(self):
        print('MEOW!')


class AbstractExample:
    def __init__(self):
        pass

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


def inheritance_example():
    animal_list = [Dog(), Cat()]

    for pet in animal_list:
        pet.speak()
