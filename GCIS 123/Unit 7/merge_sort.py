'''
    7.15 Lecture
    Author: Sam Sit
'''

import arrays
import array_utils

def merge_sort(an_array):
    if len(an_array) < 2:
        return an_array

def split(an_array):
    total = len(an_array)
    
    if total % 2:
        evens = arrays.Array(int(total/2+1))
    else:
        evens = arrays.Array(int(total/2))
    odds = arrays.Array(int(total/2))

    for i in range(total):
        if i%2:
            print(i)
            odds[int(i/2)] = an_array[i]
        else:
            evens[int(i/2)] = an_array[i]

    return evens, odds

def main():

    an_array = array_utils.range_array(0, 10)
    print(split(an_array))

main()