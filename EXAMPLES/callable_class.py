#!/usr/bin/env python

class HTMLWrapper():

    def __init__(self, tag):
        self._tag = tag

    def __call__(self, text):  # <1>
        return '<{0}>{1}</{0}>'.format(self._tag, text)

if __name__ == '__main__':
    h1 = HTMLWrapper('h1')  # <2>
    print(h1('spam'))  # <3>
    div = HTMLWrapper('div')
    print(div('ham'))

    fragment = div(h1("wombat"))
    print(fragment)

