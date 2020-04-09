#!/usr/bin/env python

class StupidGen:
    def __init__(self):
        self.index = 0
        self.data = ['red', 'blue', 'green']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        old_index = self.index
        self.index += 1
        return self.data[old_index]

sg = StupidGen()
for x in sg:
    print(x)
print()

class PresidentsByParty:
    def __init__(self, party):
        self.party = party
        self.pres_in = open('DATA/presidents.txt')

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            raw_line = next(self.pres_in)
            if raw_line == '':
                raise StopIteration
            fields = raw_line.rstrip().split(':')
            if fields[-1] == self.party:
                return fields

dems = PresidentsByParty('Democratic')
for pres in dems:
    print(pres)
print()

whigs = PresidentsByParty('Whig')
for pres in whigs:
    print(pres)
