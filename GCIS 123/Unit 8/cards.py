'''
    8.1 Assignment
    Author: Sam Sit
'''

import random

def make_card(rank, suit):
    rankWord = rank
    shortChar = rank
    shortSuit = suit[0]
    red = "\033[31m"
    blue = "\033[34m"
    norm = "\033[37m"

    if rank == 11:
        rankWord = "Jack"
        shortChar = "J"
    elif rank == 12:
        rankWord = "Queen"
        shortChar = "Q"
    elif rank == 13:
        rankWord = "King"
        shortChar = "K"
    elif rank == 14:
        rankWord = "Ace"
        shortChar = "A"
    rank = str(rank)
    
    name = str(rankWord) + " of " + suit

    shorthand = str(shortChar) + shortSuit
    if len(shorthand) == 2:
        shorthand = " " + shorthand

    if shortSuit == "S" or shortSuit == "C":
        shorthand = blue + shorthand + norm
    else:
        shorthand = red + shorthand + norm

    result = (rank, suit, name, shorthand)
    return result

def make_deck():
    deck = []
    for i in range(4):
        suit = "Spades"
        if i == 1:
            suit = "Hearts"
        elif i == 2:
            suit = "Clubs"
        elif i == 3:
            suit = "Diamonds"
        for j in range(13):
            deck.append(make_card(j+2, suit))
    return deck

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def shuffle(deck):
    for i in range(len(deck)-1):
        j = random.randint(i, 51)
        swap(deck, i, j)
    return deck

def draw(deck, hand):
    if len(deck) == 0:
        return None
    else:
        #cardNum = random.randint(0,len(deck)-1)
        cardNum=len(deck)-1
        card = deck[cardNum]
        deck.pop(cardNum)
        hand.append(card)
    return card

def deal_one_hand(deck, num):
    hand = []
    for i in range(num):
        draw(deck, hand)[3]
    return hand