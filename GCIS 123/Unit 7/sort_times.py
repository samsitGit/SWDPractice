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
    return elapsed

def main():
    print("now testing with size 3000 arrays")
    #sorted already
    array1 = array_utils.range_array(1, 3000)
    print("sorted:", insertion_sort_function_timer(array1))
    #random elements
    array2 = array_utils.random_array(3000)
    print("random:", insertion_sort_function_timer(array2))
    #sorted reversely
    array3 = array_utils.range_array(1, 3000)
    array3 = sorts.insertion_sort_reverse(array3)
    print("reverse:", insertion_sort_function_timer(array3))

main()