#!/usr/bin/env python
from pyparsing import *

# http://bob:secret@some.host.com:1234/more/path?p1=v1&p2=v2

'''   
URL grammar
   url ::= scheme '://' [userinfo] host [port] [path] [query] [fragment]
   scheme ::= http | https | ftp | file
   userinfo ::= url_chars+ ':' url_chars+ '@'
   host ::= alphanums | host (. + alphanums)
   port ::= ':' nums
   path ::= url_chars+
   query ::= '?' + query_pairs
   query_pairs ::= query_pairs | (query_pairs '&' query_pair)
   query_pair = url_chars+ '=' url_chars+
   fragment = '#' + url_chars
   url_chars = alphanums + '-_.~%+'
'''  # <1>

url_chars = alphanums + '-_.~%+'  # <2>

fragment  = Combine((Suppress('#') + Word(url_chars)))('fragment')  # <3>

scheme = oneOf('http https ftp file')('scheme')   # <4>
host = Combine(delimitedList(Word(url_chars), '.'))('host')  # <5>
port = Suppress(':') + Word(nums)('port')   # <6>
user_info = (   # <7>
    Word(url_chars)('username')    # <8>
    + Suppress(':')                # <9>
    + Word(url_chars)('password')  # <10>
    + Suppress('@')                # <11>
)
query_pair = Group(Word(url_chars) + Suppress('=') + Word(url_chars))  # <12>
query = Group(Suppress('?') + delimitedList(query_pair, '&'))('query')  # <13>

path = Combine(
    Suppress('/')
    + OneOrMore(~query + Word(url_chars + '/'))
)('path')  # <14>

url_parser = (
    scheme
    + Suppress('://')
    + Optional(user_info)
    + host
    + Optional(port)
    + Optional(path)
    + Optional(query)
    + Optional(fragment)
)   # <15>
