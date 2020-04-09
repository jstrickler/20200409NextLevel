#!/usr/bin/env python

def get_pres_by_party(party_wanted):
    with open('DATA/presidents.txt') as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip() # remove \n
            term, first_name, last_name, birthplace, birth_state, birth_date, death_date, took_office, left_office, party = line.split(':')
            if party == party_wanted:
                yield term, first_name, last_name, birthplace, birth_state, birth_date, death_date, took_office, left_office, party


gop  = get_pres_by_party('Republican')

print(gop)
for p in gop: # next()
    print(p)
print('-' * 60)


