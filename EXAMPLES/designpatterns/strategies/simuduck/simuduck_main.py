#!/usr/bin/env python
# (c)2015 John Strickler

from duck import Duck
from quacklib import MuteQuack, Squeak
from flylib import Flightless

class Beeper():
    def quack(self):
        print("Beep! Beep!")


d1 = Duck('Mallard')
d2 = Duck('Robot', quack=Beeper())
d3 = Duck('Rubber Duckie', quack=Squeak(), fly=Flightless())

for d in d1, d2, d3:
    d.display()
    d.quack()
    d.fly()
    print('-' * 60)
