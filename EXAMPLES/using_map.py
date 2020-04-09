#!/usr/bin/env python
#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # <1>
print(result)

result = list(map(str.upper, strings))  # <2>
print(result)

result = list(map(len, strings))  # <3>
print(result)
