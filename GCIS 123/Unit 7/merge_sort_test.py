'''
    7.15 Lecture
    Author: Sam Sit
    ex. python -m pytest -s .\merge_sort_test.py::test_merge_sort
'''

import array_utils
import merge_sort

def test_merge_sort0():
    #set up
    array = array_utils.random_array(0)
    expected = array

    #invoke
    result = merge_sort.merge_sort(array)

    #analyze
    assert result == expected

def test_merge_sort1():
    #set up
    array = array_utils.random_array(1)
    expected = array

    #invoke
    result = merge_sort.merge_sort(array)

    #analyze
    assert result == expected