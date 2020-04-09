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

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fgen = (f.upper() for f in fruits)
print(fgen)
print(islice(fgen, 3, 8))
for i in islice(fgen, 3, 8):
    print(i)

print(list(fgen))


print(repeat('wow', 10))
