#!/usr/bin/env python


class debugger():  # <1>

    function_calls = []

    def __init__(self, func):  # <2>
        self._func = func

    def __call__(self, *args, **kwargs):  # <3>

        # print("*" * 40)  # <4>
        # print("function {}()".format(self._func.__name__))  # <4>
        # print("\targs are ", args)  # <4>
        # print("\tkwargs are ", kwargs)  # <4>
        #
        # print("*" * 40)  # <4>

        self.function_calls.append(  # <5>
            (self._func.__name__, args, kwargs)
        )

        result = self._func(*args, **kwargs)  # <6>
        return result # <7>

    @classmethod
    def get_calls(cls): # <8>
        return cls.function_calls

@debugger  # <9>
def hello(greeting, whom="world"):
    print("{}, {}".format(greeting, whom))

@debugger  # <9>
def bark(bark_word, *, repeat=2):
    print("{0}! ".format(bark_word) * repeat)

hello('hello', 'world')  # <10>
print()

hello('hi', 'Earth')
print()

hello('greetings')

bark("woof", repeat=3)
bark("yip", repeat=4)
bark("arf")

hello('hey', 'girl')

print('-' * 60)

for i, info in enumerate(debugger.get_calls(), 1):  # <11>
    print("{:2d}. {:10s} {!s:20s} {!s:20s}".format(i, info[0], info[1], info[2]))
