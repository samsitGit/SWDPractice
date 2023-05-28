'''
    8.1 Assignment
    Author: Sam Sit
    ex. 
    python -m pytest -s .\cards_test.py
'''

import cards as c
red = "\033[31m"
blue = "\033[34m"
norm = "\033[37m"

def test_make_card_1():
    #set up
    expected = ("3", "Clubs", "3 of Clubs", blue+" 3C"+norm)

    #invoke
    result = c.make_card(3, "Clubs")

    #analyze
    assert result == expected

def test_make_card_10():
    #set up
    expected = ("10", "Clubs", "10 of Clubs", blue+"10C"+norm)

    #invoke
    result = c.make_card(10, "Clubs")

    #analyze
    assert result == expected

def test_make_card_J():
    #set up
    expected = ("11", "Clubs", "Jack of Clubs", blue+" JC"+norm)

    #invoke
    result = c.make_card(11, "Clubs")

    #analyze
    assert result == expected

def test_make_card_Q():
    #set up
    expected = ("12", "Diamonds", "Queen of Diamonds", red+" QD"+norm)

    #invoke
    result = c.make_card(12, "Diamonds")

    #analyze
    assert result == expected

def test_make_card_K():
    #set up
    expected = ("13", "Hearts", "King of Hearts", red+" KH"+norm)

    #invoke
    result = c.make_card(13, "Hearts")

    #analyze
    assert result == expected

def test_make_card_A():
    #set up
    expected = ("14", "Spades", "Ace of Spades", blue+" AS"+norm)

    #invoke
    result = c.make_card(14, "Spades")

    #analyze
    assert result == expected