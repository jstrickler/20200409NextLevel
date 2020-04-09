#!/usr/bin/env python
from pyparsing import *

def upper_case_it(tokens):  # <1>
    return [t.upper() for t in tokens]

prefix = 'A Fist Full of '  # <2>

fist_contents = Word(alphas + ' ')  # <3>

fist_contents.setParseAction(upper_case_it)  # <4>

title_parser = Combine(prefix + fist_contents)  # <5>

titles = (
    'A Fist Full of Dollars',
    'A Fist Full of Spaghetti',
    'A Fist Full of Wombats',
    'A Fist Full of Jelly Beans',
    'A Fist Full of Clint Eastwood Movies',
)

for title in titles:
    print(title_parser.parseString(title)[0])  # <6>
