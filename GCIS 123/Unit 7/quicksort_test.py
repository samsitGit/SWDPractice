'''
    7.25 Lecture
    Author: Sam Sit
    ex. python -m pytest -s .\merge_sort_test.py::test_merge_sort
'''

import array_utils
import quicksort
import arrays

def test_quicksort0():
    #set up
    array = array_utils.random_array(0)
    expected = array

    #invoke
    result = quicksort.quicksort(array)

    #analyze
    assert result == expected

def test_quicksort1():
    #set up
    array = array_utils.random_array(1)
    array[0] = 1
    expected = array_utils.random_array(1)
    expected[0] = 1
    expected = array

    #invoke
    result = quicksort.quicksort(array)

    #analyze
    assert result == expected