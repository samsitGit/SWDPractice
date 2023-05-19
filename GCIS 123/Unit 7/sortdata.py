'''
    7.1 Assignment - Naive Sorts
    Author: Sam Sit
'''

import arrays
import array_utils
import sorts

#1
def sort_col(filepath, i_col, size):
    array = arrays.Array(size)
    count = 0
    with open(filepath) as file:
        next(file)
        for line in file:
            stripped = line.split(",")
            array[count] = int(stripped[i_col])
            count += 1
    print(sorts.insertion_sort(array))

#2
def insertion_sort_backwards(an_array):
    unsorted = an_array
    count = len(an_array)-1
    result = an_array
    for i in range(len(an_array)):
        sorted = arrays.Array(i+1)
        unsorted[count] = sorted[0]
        shift_backwards(sorted, i)
        count -= 1

        result = cat(unsorted,sorted)
        print(result)
        
    return result

def shift_backwards(an_array, index):
    for i in range(index):
        if an_array[index-i-1] > an_array[index-i]:
            sorts.swap(an_array, index-i-1, index-i)
        else:
            break
    return an_array

def cat(a, b):
    result = arrays.Array(len(a) + len(b))
    count = 0
    for i in range(len(a)):
        result[count] = a[i]
        count += 1
    for i in range(len(b)):
        result[count] = b[i]
        count += 1
    return result

def main():
    #sort_col("data/dataset.csv", 2, 189)
    #sort_col("data/dataset.csv", 7, 189)
    array = arrays.Array(5)
    array[0] = 5
    array[1] = 3
    array[2] = 7
    array[3] = 4
    array[4] = 1
    print(array)
    print(insertion_sort_backwards(array))

main()