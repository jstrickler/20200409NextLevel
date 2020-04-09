#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            if line.endswith('\n'):
                line = line.rstrip('\n\r')
            yield line  # <1>


for trimmed_line in trimmed('../DATA/mary.txt'):  # <2>
    print(trimmed_line)
