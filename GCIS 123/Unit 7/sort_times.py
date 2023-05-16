'''
    7.7 Lecture
    Author: Sam Sit
'''

import sorts
import time
import array_utils

def insertion_sort_function_timer(an_array):
    begin = time.perf_counter()
    sorts.insertion_sort(an_array)
    end = time.perf_counter()
    elapsed = end - begin
    print("elapsed time:", elapsed)

def binary_timer():
    array = arrays_utils.range_array(1, 10000000)
    binary_search_timer(array, 1)
    binary_search_timer(array, 5000000)
    binary_search_timer(array, 10000000)


def main():
    #sorted already
    array1 = array_utils.range_array(1, 3000)
    #random elements
    array2 = array_utils.range_array(1, 3000)
    #sorted reversely
    array3 = array_utils.range_array(1, 3000)

main()