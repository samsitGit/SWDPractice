'''
    7.7, 7.9 Lecture
    Author: Sam Sit
'''

import sorts
import time
import array_utils
import plotter
import merge_sort
import quicksort

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

#7.2 assignment
def plot_sort_time_using_random_arrays(sort_function):
    plotter.new_series()
    for i in range(len(SIZES)):
        plotter.add_data_point(sort_function_timer(array_utils.random_array(SIZES[i]), sort_function))
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
    plotter.init("Insertion and merge sort", "Array Size", "Time")
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    plot_sort_time_using_random_arrays(quicksort.quicksort)
    plotter.plot()
    input("Press enter to continue...")

main()