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

    if rank == "Jack":
        rank = 11
        shortChar = "J"
    elif rank == "Queen":
        rank = 12
        shortChar = "Q"
    elif rank == "King":
        rank = 13
        shortChar = "K"
    elif rank == "Ace":
        rank = 14
        shortChar = "A"
    
    name = str(rankWord) + " of " + suit

    shorthand = str(shortChar) + shortSuit
    if len(shorthand) == 2:
        shorthand = " " + shorthand

    if shortSuit == "S" or shortSuit == "C":
        shorthand = blue + shorthand + norm
    else:
        shorthand = red + shorthand + norm

    rank = str(rank)
    result = (rank, suit, name, shorthand)
    return result