#!/usr/bin/env python
"""
decorama -- demo of 8 combinations of decorator implementation

function decorators:
    1. function without params
        decorator returns replacement
    2. function with params
        decorator returns wrapper
        wrapper returns replacement
    3. class without params
        __call__ IS replacement
    4. class with params
        __call__ RETURNS replacement

class decorators:
    5. function without params
        __call__ IS replacement
    6. function with params
    7. class without params
    8. class with params
"""

from functools import wraps, update_wrapper


def deco_one(wrapped_function):
    """
    function without params decorating a function -- the simplest case

    @deco_one
    def bar():
        pass

    same as
    bar = deco_one(bar)


    :param wrapped_function: function to decorate
    :return: replacement function
    """

    @wraps(wrapped_function)
    def _replacement(*args, **kwargs):
        print("GREETINGS from deco_one!")
        result = wrapped_function(*args, **kwargs)
        return result + 1

    return _replacement


def deco_two(value=None):
    """
    function with params decorating a function

    @deco_two('blah')
    def bar():
        pass

    same as
    bar  = deco_two('blah')(bar)
    or,
    wrapper = foo('blah')
    bar = wrapper(bar)


    :param value: decorator parameter
    :return: replacement function
    """

    def wrapper(wrapped_function):
        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_two -- value is {}!".format(value)))
            result = wrapped_function(*args, **kwargs)
            return result + 2

        return _replacement

    return wrapper


class deco_three():
    """
    class without params decorating a function

    __call__() is the replacement function

    @deco_three
    def bar():
        pass

    same as
    bar  = deco_three(bar)


    """

    def __init__(self, wrapped_function):
        self.__name__ = wrapped_function.__name__
        self._wrapped = wrapped_function

    def __call__(self, *args, **kwargs):
        print("GREETINGS from deco_three!")
        result = self._wrapped(*args, **kwargs)
        return result + 3


class deco_four():
    """
    class with params decorating a function

    __call__() RETURNS the replacement function


    @deco_four('blah')
    def bar():
        pass

    same as
    bar  = deco_four('blah')(bar)
    or,
    wrapper = deco_four('blah')
    bar = wrapper(bar)
    """

    def __init__(self, value):
        self._value = value

    def __call__(self, wrapped_function):
        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(("GREETINGS from deco_four -- value is {}!".format(self._value)))
            result = wrapped_function(*args, **kwargs)
            return result + 4

        return _replacement


print("Function decorators:")


@deco_one
@deco_two('APPLE')
@deco_three
@deco_four('BANANA')
def target_function(color, value):
    print(("Hello from target_function -- color is {} and value is {}".format(color, value)))
    print(("Target function's name is", target_function.__name__))
    return 10 * value


tf_result = target_function('red', 10)
print(("RESULT is", tf_result))
print(('-' * 50))
tf_result = target_function('green', 45)
print(("RESULT is", tf_result))
print(('-' * 50))
print()
print()


def deco_five(target_class):
    """
    function without params decorating a class

    :param target_class: class to be decorated
    :return: modified class
    """
    print("GREETINGS from deco_five!")

    @property
    def _temp(self):
        return self._value1

    target_class.value_one = _temp

    return target_class


def deco_six(fruit):
    """
    function with params decorating a class; returns wrapper which is applied to target class

    :param fruit:
    :return: modified class
    """
    print("GREETINGS from deco_six!")

    def wrapper(target_class):
        target_class._fruit = fruit

        @property
        def _temp(self):
            return self._fruit

        target_class.fruit = _temp

        return target_class

    return wrapper


@deco_five
@deco_six('MANGO')
class target_class():

    def __init__(self, v1, v2, v3, v4):
        self._value1 = v1
        self._value2 = v2
        self._value3 = v3
        self._value4 = v4


t1 = target_class('fee', 'fi', 'fo', 'fum')
print(("t1 is", t1))
print(("value_one:", t1.value_one))

print(('-' * 50))
t2 = target_class('eeny', 'meeny', 'miny', 'mo')
print(("t2:", t2))
print(("t2.value_one:", t2.value_one))
print(("t2.fruit:", t2.fruit))

print(('-' * 50))


class deco_seven():
    """
    class without params decorating a class

    __new__() returns the modified class (not __init__, because __init__ is *instance* initializer)

    """

    def __new__(cls, old_class):
        print("GREETINGS from deco_seven!")
        old_class.color = 'blue'
        return old_class


@deco_seven
class target_class():
    pass


t1 = target_class()
print((t1.color))
print(("t1 id:", id(t1)))
print((target_class.__name__, t1))

t2 = target_class()
print((t2.color))
print(("t2 id:", id(t2)))

print(('-' * 50))


class deco_eight():
    """
    class with params decorating a class

    __call__() returns the modified class
    """

    def __init__(self, color):
        print("GREETINGS from deco_eight!")
        self._color = color

    def __call__(self, old_class):
        old_class.color = self._color
        return old_class


@deco_eight('purple')
class target_class():
    pass


t1 = target_class()
print((t1.color))
