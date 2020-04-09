#!/usr/bin/env python

from pp_url_parser import url_parser  # <1>

test_urls = [
  'http://www.notarealsite.com',
  'http://www.notarealsite.com/',
  'http://www.notarealsite.com:1234/',
  'http://bob:%243cr3t@www.notarealsite.com:1234/',
  'http://www.notarealsite.com/presidents',
  'http://www.notarealsite.com/presidents/byterm?term=26&name=Roosevelt',
  'http://www.notarealsite.com/presidents/26',
  'http://www.notarealsite.com/us/indiana/gary/population',
  'ftp://ftp.info.com/downloads',
  'http://www.notarealsite.com#moose',
  'http://bob:s3cr3t@www.notarealsite.com:8080/presidents/byterm?term=26&name=Roosevelt#bio',
]

fmt = '{:10s} {}'

for test_url in test_urls:
  print("URL:", test_url)
  tokens = url_parser.parseString(test_url)  # <2>

  print(tokens, '\n')
  print(fmt.format("Scheme:", tokens.scheme))  # <3>
  print(fmt.format("User name:", tokens.username))
  print(fmt.format("Password:", tokens.password))
  print(fmt.format("Host:", tokens.host))
  print(fmt.format("Port:", tokens.port))
  print(fmt.format("Path:", tokens.path))
  print("Query:")
  for key, value in tokens.query:
    print("\t{} ==> {}".format(key, value))
  print(fmt.format('Fragment:', tokens.fragment))
  print('-' * 60, '\n')
