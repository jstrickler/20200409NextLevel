#!/usr/bin/env python

from itertools import groupby

with open('../DATA/words.txt') as words_in:  # <1>
    all_words = (w.rstrip() for w in words_in)  # <2>

    g = groupby(all_words, key=lambda e: e[:2])  # <3>

    # print(g)
    # for letter, letter_list in g:
    #     print(letter, len(list(letter_list)))

    counts = {letter: len(list(wlist)) for letter, wlist in g}  # <4>

# sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)  # <5>
for letter, count in counts.items():  # <6>
    print(letter, count)

print()
print("Total words counted:", sum(counts.values()))  # <7>
