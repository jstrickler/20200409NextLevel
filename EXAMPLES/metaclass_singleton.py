#!/usr/bin/env python

class Singleton(type): # <1>
    _instances = {}  # <2>

    def __new__(typ, *junk):
        # print("__new__()")
        return super().__new__(typ, *junk)

    def __call__(cls, *args, **kwargs):  # <3>
        # print("__call__()")
        if cls not in cls._instances:    # <4>
            cls._instances[cls] = super().__call__(*args, **kwargs)  # <5>

        return cls._instances[cls]   # <6>


class ThingA(metaclass=Singleton):   # <7>
    def __init__(self, value):
        self.value = value


class ThingB(metaclass=Singleton):   # <7>
    def __init__(self, value):
        self.value = value


ta1 = ThingA(1)  # <8>
ta2 = ThingA(2)
ta3 = ThingA(3)

tb1 = ThingB(4)
tb2 = ThingB(5)
tb3 = ThingB(6)

for thing in ta1, ta2, ta3, tb1, tb2, tb3:
    print(type(thing).__name__, id(thing), thing.value)  # <9>
