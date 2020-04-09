#!/usr/bin/env python
from pprint import pprint
import sys
import requests
import re


BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>


def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},
    )  # <3>

    if response.status_code == requests.codes.OK:
        # pprint(response.content.decode())
        # print('-' * 60)
        words = []  # list of Word objects
        data = response.json()  # <4>
        for entry in data: # <5>
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    word_name = meta.get("id")
                    if "shortdef" in entry:
                        word_definition = '\n'.join(entry['shortdef'])
                    else:
                        word_definition = None

                    def init(self, name, definition):
                        self._name = name
                        self._definition = definition

                    name_prop = property(lambda self: self._name)
                    def_prop = property(lambda self: self._definition)

                    word = type(clean_word(word_name), (), {'__init__': init, 'definition': def_prop, 'name': name_prop})

                    words.append(word(word_name, word_definition))
    else:
        print("Sorry, HTTP response", response.status_code)

    for word in words:
        print(word, f"{word.name.upper()}:\n{word.definition}\n")

def clean_word(w):
    return re.sub(r"\W+", "_", w)



if __name__ == '__main__':
    main(sys.argv[1:])
