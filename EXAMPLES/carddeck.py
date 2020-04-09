#!/usr/bin/env python
"""
Classes for playing cards
"""
from dataclasses import dataclass, field, InitVar
from typing import List, ClassVar
import random
from pprint import pprint

@dataclass
class Card:
    """
    One playing card with rank and suit
    """
    rank: str
    suit: str

    def __repr__(self):
        return f"{self.rank}-{self.suit}"

@dataclass
class CardDeck:
    """
    A standard deck of playing cards
    """
    SUITS: ClassVar = "Clubs Diamonds Hearts Spades".split()
    RANKS: ClassVar = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    cards: List[Card] = field(init=False, default_factory=list, repr=False)

    dealer: str
    _dealer: str = field(init=False, repr=False)

    def __post_init__(self):
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                card = Card(rank, suit)
                self.cards.append(card)

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise ValueError(f"Dealer must be string, not {type(value).__name__}")

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


if __name__ == '__main__':
    d = CardDeck("Bob")
    print(d)
    try:
        x = CardDeck(123)
    except ValueError as err:
        print(err)

    d.shuffle()

    print("Cards:", end=' ')
    pprint(d.cards)
    print()

    print("Drawing:")
    for _ in range(10):
        print(d.draw())
    print()

    print(d.dealer)
