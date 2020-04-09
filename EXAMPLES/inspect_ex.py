#!/usr/bin/env python
import typing as T
import inspect
import pandas as pd

class Dog:
    pass

class Spam:  # <1>
    pass


def ham(p1: int, p2: str= 'a', *p3, p4: float, p5: str= 'b', **p6) -> None:  # <2>
    print(p1, p2, p3, p4, p5, p6)

Numeric = T.Union[int, float]

def toast(a: T.Any, b: Numeric, c: T.Iterable) -> T.Union[T.Iterable, None]:
    pass

def update(df: pd.DataFrame) -> pd.DataFrame:
    pass

def groom(d: Dog):
    pass

for thing in (inspect, Spam, ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
    ))

ham("abc", 5, 6, 8, 'jabberwocky', p4='fud', p5=12)

print()

print("Function spec for Ham:", inspect.getfullargspec(ham))  # <6>
print()

print("Arg spec for toast:", inspect.getfullargspec(toast), '\n')

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>
