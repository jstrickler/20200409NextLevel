#!/usr/bin/env python

def snake_to_camel(name):
    words = name.split('_')
    new_words = [w.capitalize() for w in words]
    return ''.join(new_words)


if __name__ == '__main__':
    test_strings = [
        "test_case",
        "wombat_nest",
        "blue_meany",
        "JunkFile",
        "blorb",
    ]

    for t in test_strings:
        print("{:12s} {}".format(t, snake_to_camel(t)))

