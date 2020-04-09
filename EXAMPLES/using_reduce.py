#!/usr/bin/env python
#
from operator import add, mul
from functools import reduce

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# sum()
result = reduce(add, values) # <1>
print("result is", result)

# sum() + 1000
result = reduce(add, values, 1000)  # <2>
print("result is", result)

# product
result = reduce(mul, values)  # <3>
print("result is", result)

strings = ['fi', 'fi', 'fo', 'fum']

# join
result = reduce(add, strings, "") # <4>
print("result is", result)

# join + upper case
result = reduce(add, map(str.upper, strings), "")  # <5>
print("result is", result)
