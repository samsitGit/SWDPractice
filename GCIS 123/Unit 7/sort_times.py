'''
    7.7, 7.9 Lecture
    Author: Sam Sit
'''

import sorts
import time
import array_utils

SIZES = array_utils.range_array(200,2001,300)

''' #pre 7.9
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
    
'''
#7.9
def sort_function_timer(an_array, sort_function):
    begin = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()
    elapsed = end - begin
    return elapsed



def main():
    '''
    print("now testing with size 3000 arrays")
    #random elements
    array1 = array_utils.random_array(3000)
    array2 = array1
    print("insertion sort (swaps):", sort_function_timer(array1, sorts.insertion_sort))
    print("insertion sort (no swaps):", sort_function_timer(array2, sorts.insertion_sort_wo_swap))
    '''
    #7.2 assignment
    print(SIZES)

main()