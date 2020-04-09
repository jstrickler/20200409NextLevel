#!/usr/bin/env python
#
from itertools import islice, count, cycle, repeat

for i in count(0, 10):  # <1>
    if i > 50:
        break  # <2>
    print(i, end=' ')
print("\n")

for i in islice(count(0, 10), 6):  # <3>
    print(i, end=' ')
print("\n")

giant = ['fee', 'fi', 'fo', 'fum']

for i in islice(cycle(giant), 10):  # <4>
    print(i, end=' ')
print("\n")

for i in repeat('tick', 10):  # <5>
    print(i, end=' ')
print("\n")
