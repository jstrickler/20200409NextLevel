#!/usr/bin/env python
from types import MethodType

class Dog(): # <1>
    pass

d1 = Dog()  # <2>

def bark(self):  # <3>
    print("Woof! woof!")

setattr(Dog, "bark", bark)  # <4>

d2 = Dog() # <5>

d1.bark()  # <6>
d2.bark()

def wag(self): # <7>
    print("Wagging...")

setattr(d1, "wag", MethodType(wag, d1))  # <8>

d1.wag()  # <9>
try:
    d2.wag()  # <10>
except AttributeError as err:
    print(err)
