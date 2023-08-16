# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 07:08:17 2023

@author: Teja Ram Pooniya
@Program: Cards __init__ and __len__ and __getitem__ 
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
        def __len__(self):
            return len(self._cards)
        
        def __getitem__(self, position):
            return self._cards[position]
        
# Terminal: beer_card = Card('7', 'diamonds')
# Terminal: beer_card
# Terminal[output]: Card(rank='7' suit='diamonds')
