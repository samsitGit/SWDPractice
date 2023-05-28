'''
    8.1 Assignment
    Author: Sam Sit
'''

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
    for i in range(4):
        for j in range(13):
            print(i)