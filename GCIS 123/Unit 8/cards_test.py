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