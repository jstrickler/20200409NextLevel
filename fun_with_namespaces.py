#!/usr/bin/env python

x = 1234   #  global

class Toast:
    pass

def spam():  # global
    x = 5.6  # local???
    y = "wombat"    # local
    print("in spam(): x is", x)
    print("in spam(): GLOBAL x is", globals()['x'])

    def ham():
        pass

    print("locals:", locals(), '\n')

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




