#!/usr/bin/env python

from datetime import date

dates = [
    (1968, 10, 11),
    (1968, 12, 21),
    (1969, 3, 3),
    (1969, 5, 18),
    (1969, 7, 16),
    (1969, 11, 14),
    (1970, 4, 11),
    (1971, 1, 31),
    (1971, 7, 26),
    (1972, 4, 16),
    (1927, 12, 7),
]  # <1>

# for dt in dates:
#     d = date(*dt)  # <2>  turns  date(TUPLE)  into date(p1, p2, p3)
#     print(d)
date_list = [date(*dt) for dt in dates]
print(date_list)

print()

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
          "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear",
          "banana", "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry",
          "lychee", "grape"]

sort_opts = {
    'key': lambda e: e.lower(),
    'reverse': True,
}  # <3>

sorted_fruits = sorted(fruits, **sort_opts)  # <4>  # equal to  sorted(fruits, key=lambda ..., reverse=True)
print(sorted_fruits)
