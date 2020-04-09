#!/usr/bin/env python

def function_1(self):  # <1>
    print("Hello from f1()")


def function_2(self):  # <1>
    print("Hello from f2()")


NewClass = type("NewClass", (), {  # <2>
    'hello1': function_1,
    'hello2': function_2,
    'color': 'red',
    'state': 'Ohio',
})

n1 = NewClass()  # <3>

n1.hello1()  # <4>
n1.hello2()
print(n1.color)  # <5>
print()

SubClass = type("SubClass", (NewClass,), {'fruit': 'banana'})  # <6>
s1 = SubClass()  # <7>
s1.hello1()  # <8>
print(s1.color)  # <9>
print(s1.fruit)
