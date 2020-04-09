#!/usr/bin/env python

def void(old_function):
    return 42  # <1>

name = "Guido"
x = void(name)

@void  # <2>
def hello():
    print("Hello, world")

print(hello, type(hello)) # <3>
print(x, type(x))
