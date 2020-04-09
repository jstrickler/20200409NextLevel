#!/usr/bin/env python

class Foo:
    pass

f = Foo()
print(type(f))

t = type(f)

x = t()
print(x)

# type(....)
Animal = type("Animal", (), {'walk': lambda self: print("walking...")})

Dog = type('Dog', (Animal,), {'wag': lambda self: print("wagging...")})

d1 = Dog()
d2 = Dog()
d2.wag()
d1.walk()

