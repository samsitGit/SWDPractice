'''
    7.25 Lecture
    Author: Sam Sit
    skipping next lectures as it seems to be duplicates
    then the same old tests
'''

import arrays
import array_utils

def quicksort(an_array):
    if len(an_array) < 2:
        return an_array
    else:
        pivot = an_array[0]
        less, same, more = partition(pivot, an_array)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)

        result = arrays.Array(len(less) + len(same) + len(more))
        resultCount = 0
        for i in range(len(less)):
            result[resultCount] = sorted_less[i]
            resultCount+=1

        for i in range(len(same)):
            result[resultCount] = same[i]
            resultCount+=1

        for i in range(len(more)):
            result[resultCount] = sorted_more[i]
            resultCount+=1

        return result

def partition(pivot, an_array):
    less_count = 0
    same_count = 0
    more_count = 0

    for i in range(len(an_array)):
        if an_array[i] < pivot:
            less_count += 1

        elif an_array[i] > pivot:
            more_count += 1
        else:
            same_count += 1

    lcounter = 0
    scounter = 0
    mcounter = 0

    less = arrays.Array(less_count)
    same = arrays.Array(same_count)
    more = arrays.Array(more_count)

    for i in range(len(an_array)):
        if an_array[i] < pivot:
            less[lcounter] = an_array[i]
            lcounter += 1

        elif an_array[i] > pivot:
            more[mcounter] = an_array[i]
            mcounter += 1
        else:
            same[scounter] = an_array[i]
            scounter += 1
    return less, same, more