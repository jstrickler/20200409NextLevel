#!/usr/bin/env python
# (c) 2016 John Strickler
#

class FlyWeight(object):
    def __init__(self, cls):
        self._cls = cls
        self._instances = dict()

    def __call__(self, *args, **kargs):
        return self._instances.setdefault(
            (args, tuple(kargs.items())),
            self._cls(*args, **kargs)
        )

