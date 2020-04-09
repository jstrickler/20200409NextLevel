#!/usr/bin/env python
from datetime import datetime
from functools import wraps

def timestamp(func):

    @wraps(func)
    def _(*args, **kwargs):
        print(func.__name__, datetime.now())
        result = func(*args, **kwargs)
        return result

    return _

@timestamp
def foo():
    """
    The foo function

    :return:
    """
    print("calling foo()")

@timestamp
def bar():
    """
    The bar function

    :return:
    """
    print("calling bar()")

foo()
bar()
foo()
foo()

print()
print(foo.__name__)
print(bar.__name__)

# @register_handler
# def my_handler():
#     pass

# some_pkg.register_handler(my_handler)
