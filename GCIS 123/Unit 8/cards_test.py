'''
    8.1 Assignment
    Author: Sam Sit
    ex. python -m pytest -s .\merge_sort_test.py::test_merge_sort
'''

import cards as c

def test_make_card_1():
    #set up
    expected = ("3", "Clubs", "3 of Clubs", " 3C")

    #invoke
    result = c.make_card(3, "Clubs")

    #analyze
    assert result == expected

def test_make_card_10():
    #set up
    expected = ("10", "Clubs", "10 of Clubs", "10C")

    #invoke
    result = c.make_card(10, "Clubs")

    #analyze
    assert result == expected

def test_make_card_J():
    #set up
    expected = ("11", "Clubs", "Jack of Clubs", " JC")

    #invoke
    result = c.make_card("Jack", "Clubs")

    #analyze
    assert result == expected

def test_make_card_Q():
    #set up
    expected = ("12", "Diamonds", "Queen of Diamonds", " QD")

    #invoke
    result = c.make_card("Queen", "Diamonds")

    #analyze
    assert result == expected

def test_make_card_K():
    #set up
    expected = ("13", "Hearts", "King of Hearts", " KH")

    #invoke
    result = c.make_card("King", "Hearts")

    #analyze
    assert result == expected

def test_make_card_A():
    #set up
    expected = ("14", "Spades", "Ace of Spades", " AS")

    #invoke
    result = c.make_card("Ace", "Spades")

    #analyze
    assert result == expected