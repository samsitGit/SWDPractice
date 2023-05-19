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

def test_quicksort2():
    #set up
    array = array_utils.random_array(3)
    array[0] = 3
    array[1] = 1
    array[2] = 2
    expected = array_utils.random_array(3)
    expected[0] = 1
    expected[1] = 2
    expected[2] = 3
    expected = array

    #invoke
    result = quicksort.quicksort(array)

    #analyze
    assert result == expected