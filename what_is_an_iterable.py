#!/usr/bin/env python

a = 1, 2, 3
b = [4, 5, 6]  # is not an iterator, but HAS an iterator
c = "789"
d = {10: "foo", 11: "bar", 12: "blah"}
e = range(10)
f = enumerate(b)
g = reversed(a)

ia = iter(a)  #  __iter__() method which returns the iterator
ib = iter(b)
ic = iter(c)

print(next(ia))  # __next__() method return each successive element
print(next(ia))
print(next(ic))
print(next(ic))

with open('DATA/mary.txt') as myfile_in:
    header_line = next(myfile_in).rstrip()  # read 1st line
    print("header:", header_line)
    for raw_line in myfile_in:
        print(raw_line.rstrip())


