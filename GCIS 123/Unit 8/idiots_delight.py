'''
    8.2 Assignment
    Author: Sam Sit
'''

import cards as c

def deal_hand():
    deck = c.make_deck()
    deck = c.shuffle(deck)
    hand = c.deal_one_hand(deck, 4)
    return deck, hand

def discard(hand, num):
    if num != 2 and num != 4 and len(hand) < 4:
        return hand
    elif num == 4:
        for i in range(4):
            hand.pop(len(hand)-1)
        return hand
    elif num == 2:
        hand.pop(1)
        hand.pop(1)
        return hand
    
def play_round(deck, hand):
    while len(hand) < 4:
        card = c.draw(deck, hand)
        if card == None:
            return deck, hand
        for i in hand:
            print(i[3], end = " ")
        print("drew a card")
    card = c.draw(deck, hand)
    if card == None:
        return deck, hand
    for i in hand:
        print(i[3], end = " ")
    print()

    discarded = True
    while len(hand) >= 4 and discarded == True:
        if(hand[len(hand)-1][0] == hand[len(hand)-4][0]):
            hand = discard(hand, 4)
        elif(hand[len(hand)-2][0] == hand[len(hand)-3][0]):
            hand = discard(hand, 2)
        else:
            discarded = False
        
    return deck, hand

def main():
    win = False
    while win == False:
        deck, hand = deal_hand()
        startHand = hand
        count = 0
        while len(deck) > 0:
            count += 1
            print("Round", count)
            play_round(deck, hand)
        print("You have", len(hand), "cards left in your hand.")
        if len(hand) == 0:
            print("You have won!")
            win = True
        else:
            print("You've lost, please try again!")
    
main()