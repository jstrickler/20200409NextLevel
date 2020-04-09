#!/usr/bin/env python

from functools import wraps


def debugger(old_func):  # <1>

    @wraps(old_func)  # <2>
    def new_func(*args, **kwargs):  # <3>
        print("*" * 40)  # <4>
        print("** function", old_func.__name__, "**")  # <4>

        if args:  # <4>
            print("\targs are ", args)
        if kwargs:  # <4>
            print("\tkwargs are ", kwargs)

        print("*" * 40)  # <4>

        return old_func(*args, **kwargs)  # <5>

    return new_func  # <6>


@debugger  # <7>
def hello(greeting, whom='world'):
    print("{}, {}".format(greeting, whom))


hello('hello', 'world')  # <8>
print()

hello('hi', 'Earth')
print()

hello('greetings')
