'''
    7.15-18 Lecture
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

def merge(sorted1, sorted2):

    length = len(sorted1) + len(sorted2)

    result = arrays.Array(length)

    i1 = 0
    i2 = 0
    i = 0

    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] <= sorted2[i2]:
            result[i] = sorted1[i1]
            i1 += 1
        else:
            result[i] = sorted2[i2]
            i2 += 1
        i+=1
    while i1 < len(sorted1):
        for e in range(i1, len(sorted1)):
            result[i] = sorted1[i1]
            i1 += 1
            i += 1
    while i2 < len(sorted2):
        for e in range(i2, len(sorted2)):
            print("b")
            result[i] = sorted2[i2]
            i2 += 1
            i += 1
    return result

def main():

    #an_array = array_utils.range_array(0, 10)
    #print(split(an_array))
    print()

main()