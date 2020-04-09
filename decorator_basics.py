#!/usr/bin/env python

def eggs(func):
    print("in eggs(): func is", func)
    return 42

@eggs
def spam():
    print("Hello I am a spam")
# spam = eggs(spam)

# spam()
print(spam, type(spam))

def ham():
    print("ham ham ham")

ham = eggs(ham)
print(ham)

