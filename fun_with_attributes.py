#!/usr/bin/env python
class Cat:
    def __init__(self, name):
        self.name = name

    def purr(self):
        print("prrrrrrrrrr")

class Dog:

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    @property
    def breed(self):  # getter property
        return self._breed

    @breed.setter
    def breed(self, value):  # setter property
        self._breed = value

    def bark(self):
        print("woof woof")

#    def wag

d1 = Dog('mutt', 'Andy')
d2 = Dog('German Shepherd', 'Rin-tin-tin')

print(d1.breed, d1.name)

print(getattr(d1, "breed"))

animals = [d1, d2, Cat('Midnight'), Cat('Bonnie')]

for animal in animals:
    if hasattr(animal, 'bark'):
        animal.bark()
    else:
        print(animal, "can't bark")

#  getattr hasattr setattr delattr

def junk(self):
    print("wagging wagging wagging")


#      Class attr-name  attr-value
setattr(Dog, 'wag',     junk)

d1.wag()
d2.wag()

# @property  @classmethod @staticmethod
# @unittest.skip()  @unittest.skipif()
# @app.route(...)


