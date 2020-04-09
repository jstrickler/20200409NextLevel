#!/usr/bin/env python
#
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):  # <1>

    @abstractmethod   # <2>
    def speak(self):
        pass

class Dog(Animal):  # <3>
    def speak(self):   # <4>
        print("woof! woof!")

class Cat(Animal):  # <3>
    def speak(self):  # <4>
        print("Meow meow meow")

class Duck(Animal): # <3>
    pass  # <5>

d = Dog()
d.speak()

c = Cat()
c.speak()

try:
    d = Duck()  # <6>
    d.speak()
except TypeError as err:
    print(err)
