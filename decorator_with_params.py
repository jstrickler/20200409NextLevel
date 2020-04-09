#!/usr/bin/env python
from functools import wraps

# @foo
# def bar():
#    pass
#  SAME AS
# bar = foo(bar)

# @foo(a, b, c)
# def bar():
#     pass
#  SAME AS
# bar = foo(a, b, c)(bar)

def say_funny_word(funny_word):

    def _deco(old_func):

        @wraps(old_func)
        def _(*args, **kwargs):
            print(funny_word)
            result = old_func(*args, **kwargs)
            return result

        return _

    return _deco


@say_funny_word("wombat")
def spam():
    print("in spam")

@say_funny_word("wankel rotary engine")
def ham():
    print("in ham")

spam()
ham()
spam()
spam()
ham()

route_maps = {}

def route(url_path):

    def _deco(old_func):
        route_maps[url_path] = old_func

        return old_func

    return _deco


@route("/home")
def index():
    pass

@route("/wombats/zoo")
def zoo():
    pass

print(route_maps)

