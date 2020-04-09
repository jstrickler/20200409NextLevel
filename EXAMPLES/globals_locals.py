#!/usr/bin/env python
from pprint import pprint  # <1>

spam = 42  # <2>
ham = 'Smithfield'


def eggs(fruit):  # <3>
    name = 'Lancelot'  # <4>
    idiom = 'swashbuckling'  # <4>
    print("Globals:")
    pprint(globals())  # <5>
    print()
    print("Locals:")
    pprint(locals())  # <6>


eggs('mango')
