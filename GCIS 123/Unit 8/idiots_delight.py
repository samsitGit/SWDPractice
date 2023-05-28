'''
    8.2 Assignment
    Author: Sam Sit
'''

import cards as c

def deal_hand():
    deck = c.make_deck()
    hand = c.deal_one_hand(deck, 4)
    return deck, hand

def discard(hand, num):
    if num != 2 or num != 4 or len(hand) < 4:
        return hand
    elif num == 4:
        hand = ()
        return hand
    elif num == 2:
        hand.pop(1)
        hand.pop(1)
        return hand
    
def play_round(deck, hand):
    while len(hand) < 4:
        c.draw(deck, hand)
        print(hand)
    c.draw(deck, hand)
    print(hand)
    return deck, hand