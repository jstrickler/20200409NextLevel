#!/usr/bin/env python
from pyparsing import *

'''
    inifile ::= section+
    section ::= section_tag + section_data
    section_tag ::= '[' alphanums+ ']'
    section_data ::= key_value_pair+
    key_value_pair ::= key '=' value
    key ::= alphanums+
    value ::= chars+
'''

value = Word(' \t' + printables, excludeChars='=')('value')  # <1>
key = Word(alphanums)('key')  # <2>
key_value_pair = Group(key + Suppress('=') + value)  # <3>
section_data = Group(OneOrMore(key_value_pair))('keylist')  # <4>
start_tag = Suppress('[')   # <5>
end_tag = Suppress(']')   # <6>
section_tag = start_tag + Word(alphanums)('section') + end_tag  # <7>
section = Group(section_tag + section_data + Suppress(Optional(White())))  # <8>
ini_file = OneOrMore(section)  # <9>

with open('../DATA/application.ini') as ini_in:
    contents = ini_in.read()  # <10>

for section in ini_file.parseString(contents):  # <11>
    print(section.section)  # <12>
    for key, value in section.keylist:   # <13>
        print('\t{:10s} {}'.format(key, value))
