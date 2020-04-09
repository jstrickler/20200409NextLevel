#!/usr/bin/env python
try:
    from functools import singledispatch
except:
    from singledispatch import singledispatch

def foo(a: str):
    return len(a)

def foo(a: int):
    return a * 10

print(foo('abc'))
print(foo(5))

def foo(a):
    if isinstance(a, str):
        return len(a)
    elif isinstance(a, int):
        return a * 10

print(foo('abc'))
print(foo(5))

@singledispatch
def foo(a):
    raise TypeError("got unexpected type")

@foo.register(int)
def _(a):
    return a * 10

@foo.register(str)
def _(a):
    return len(a)

print(foo('definitely Python'))
print(foo(88))

print(foo.registry.items())







