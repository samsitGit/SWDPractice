'''
    8.2 Assignment
    Author: Sam Sit
'''

import cards as c

def deal_hand():
    deck = c.make_deck()
    hand = c.deal_one_hand(deck, 4)
    return deck, hand

