#!/usr/bin/env python
import sys

def print(*args):
    __builtins__.print(*args)
    # for arg in args:
    #     sys.stdout.write(str(arg).upper() + ' ')
    # sys.stdout.write('\n')

x = 1234   #  global

class Toast:
    pass

def spam() -> None:  # global
    """
    A very silly function

    :return: Nothing at all
    """
    x = 5.6  # local???
    y = "wombat"    # local
    print("in spam(): x is", x)
    print("in spam(): GLOBAL x is", globals()['x'])

    def ham():
        print("in ham: x is", x)

    print("locals:", locals(), '\n')

    # local -> nonlocal -> global -> builtin

spam()

print("in main: x is", x)

print(globals(), '\n')

g = globals()

g['animal'] = 'wombat'

print(animal, '\n')

temp_dict = {}
temp_dict.update(g)

# for name, object_type in temp_dict.items():
#     print(name, object_type)
# print()
#

some_list = []

some_other_list = ['a', 'b', 'c']

for x in some_other_list:
    # x = next(some_other_list)
    some_list.append(x)

print(some_list)

x = 1000
if x > 50:
    y = "Mickey Mouse"
print(y)

print(dir(__builtins__), '\n')

print(dir(spam))

print(spam.__doc__, '\n')

print(spam.__annotations__, '\n')


