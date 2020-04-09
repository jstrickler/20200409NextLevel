#!/usr/bin/env python
from pyparsing import *

'''  # <1>
grammar:
ssn = nums+ dash nums+ dash nums+
dash = '-'
nums = '0' | '1' | '2' etc etc
'''

dash = '-'  # <2>

ssn_parser = Combine(
    Word(nums, exact=3)  # <3>
    + dash
    + Word(nums, exact=2)
    + dash
    + Word(nums, exact=4)
)   # <4>

input_string = """
    xxx 215-72-8314 yyy
    102-46-6919 zzz 182-19-2201
"""

for matches, start, stop in ssn_parser.scanString(input_string):  # <5>
    print(matches, start, stop)


