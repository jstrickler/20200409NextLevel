#!/usr/bin/env python

class Spam():

    def eggs(self, msg):  # <1>
        print("eggs!", msg)


s = Spam()

s.eggs("fried")

print("hasattr()", hasattr(s, 'eggs'))  # <2>

e = getattr(s, 'eggs')  # <3>
e("scrambled")


def toast(self, msg):
    print("toast!", msg)


setattr(Spam, 'eggs', toast)  # <4>

s.eggs("buttered!")

delattr(Spam, 'eggs')  # <5>

try:
    s.eggs("shirred")
except AttributeError as err:  # <6>
    print(err)
