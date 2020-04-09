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
print("result is {:,d}".format(result))

x = 32_234_830_771_392

strings = ['fee', 'fi', 'fo', 'fum']

# join
result = reduce(add, strings, "") # <4>
print("result is", result)

# join + upper case
result = reduce(add, map(str.upper, strings), "")  # <5>
print("result is", result)

# map a function that triples values to a list of numbers
result = map(lambda x: x * 3, values)
print(list(result))

result = map(lambda x: x * 3, strings)
print(list(result))

result = [v * 3 for v in values]
print(result)

result = (v * 3 for v in values)
print(result)
print(list(result))




