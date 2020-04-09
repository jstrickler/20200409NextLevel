#!/usr/bin/env python
#
from itertools import product, permutations, combinations

SUITS = 'CDHS'
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = product(SUITS, RANKS)  # <1>
print(list(cards), '\n')

cards = [r + s for r, s in product(SUITS, RANKS)]  # <2>
print(cards, '\n')

giant = ['fee', 'fi', 'fo', 'fum']

result = combinations(giant, 2)  # <3>
print(list(result), "\n")

result = permutations(giant, 2)  # <4>
print(list(result), "\n")
