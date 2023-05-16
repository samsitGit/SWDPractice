'''
    7.15 Lecture
    Author: Sam Sit
'''

import array_utils
import merge_sort

def test_merge_sort(an_array):
    #set up
    array = array_utils.random_array(0)
    expected = array

    #invoke
    result = merge_sort.merge_sort(array)

    #analyze
    assert result == expected