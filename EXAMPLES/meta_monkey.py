#!/usr/bin/env python

class Spam():  # <1>

    def __init__(self, name):
        self._name = name

    def eggs(self):  # <2>
        print("Good morning, {}. Here are your delicious fried eggs.".format(self._name, ))


s = Spam('Mrs. Higgenbotham')  # <3>
s.eggs()  # <4>


def scrambled(self):  # <5>
    print("Hello, {}. Enjoy your scrambled eggs".format(self._name, ))


setattr(Spam, "eggs", scrambled)  # <6>

s.eggs()  # <7>
