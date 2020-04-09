#!/usr/bin/env python
from pyparsing import *

"""
Grammar:
email ::= name '@' domain
name ::= name | '.' name
name_part ::= (alphanumeric + '_-')+
domain ::= domain_part | '.' domain_part
domain_part ::= alphanumeric+
"""

domain_part = Word(alphanums)
domain = delimitedList(domain_part, '.', combine=True)('domain')
name_part = Word(alphanums + '_-')
name = delimitedList(domain_part, '.', combine=True)('name')
email_address = name + Suppress('@') + domain

with open('../DATA/correspondence.txt') as corr_in:
    text = corr_in.read()
    for results_list in email_address.scanString(text):
        print('Name:', results_list[0]['name'])
        print('Domain:', results_list[0]['domain'])
        print('---')


