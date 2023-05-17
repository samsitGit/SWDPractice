'''
    7.15 Lecture
    Author: Sam Sit
    ex. python -m pytest -s .\merge_sort_test.py::test_merge_sort
'''

import array_utils
import merge_sort
import arrays

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

def test_split():
    #set up
    array = array_utils.range_array(0, 9)

    expected1 = arrays.Array(5)
    expected1[0] = array[0]
    expected1[1] = array[2]
    expected1[2] = array[4]
    expected1[3] = array[6]
    expected1[4] = array[8]
    expected2 = arrays.Array(4)
    expected2[0] = array[1]
    expected2[1] = array[3]
    expected2[2] = array[5]
    expected2[3] = array[7]

    #invoke
    result1, result2 = merge_sort.split(array)

    #analyze
    assert result1 == expected1
    assert result2 == expected2

#7.20
def test_merge1():
    #set up

    sorted1 = arrays.Array(1)
    sorted1[0] = 1
    sorted2 = arrays.Array(1)
    sorted2[0] = 3
    expected = arrays.Array(2)
    expected[0] = 1
    expected[1] = 3

    #invoke
    result = merge_sort.merge(sorted1, sorted2)

    #analyze
    assert result == expected

