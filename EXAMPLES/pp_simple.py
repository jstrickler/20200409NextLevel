#!/usr/bin/env python
"""
Parse a date in the form "MMM, dd"  (using month abbreviations)
"""
import pyparsing as pp

# "bottom-up" grammar (not used by script)
"""
Date "bottom-up" grammar

Date ::= Month ', ' Day
Month ::= Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
Day ::= nums
"""

Day = pp.nums
Month = pp.oneOf('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec')
Date = Month + pp.White() + Day

samples = [
    "Feb 2",
    "Mar 5",
    "Noz 18",
    "wombat",
]

for sample in samples:
    try:
        result = Date.scanString(sample)
    except pp.ParseException as err:
        print(err)
    else:
        print(list(result))
