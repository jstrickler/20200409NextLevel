#!/usr/bin/env python
#

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]


def process_list(alist, func):  # <1>
    new_list = []
    for item in alist:
        new_list.append(func(item))  # <2>
    return new_list


f1 = process_list(fruits, str.upper)  # <3>
print(f1, "\n")

f2 = process_list(fruits, lambda s: s[0].upper())  # <4>
print(f2, "\n")

f3 = process_list(fruits, len)  # <5>
print(f3, "\n")

total_length = sum(process_list(fruits, len))  # <6>

print(total_length, "\n")
