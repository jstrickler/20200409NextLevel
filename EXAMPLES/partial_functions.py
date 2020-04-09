#!/usr/bin/env python
#
import re

from functools import partial

count_by = partial(range, 0, 25)  # <1>

print((list(count_by(1))))  # <2>  range(0, 25, 1)
print((list(count_by(3))))  # <2>  range(0, 25, 3)
print((list(count_by(5))))  # <2>
print()

has_a_number = partial(re.search, r'\d+')  # <3>

strings = [
    'abc', '123', 'abc123', 'turn it up to 11', 'blah blah'
]

for s in strings:
    print("{}:".format(s), end=' ')
    if has_a_number(s): # <4>  if re.search(r'\d+', s)
        print("YES")
    else:
        print("NO")


