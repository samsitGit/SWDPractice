import arrays
import random

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def random_sorted_array(size, min_value = 0, max_diff = None):
    an_array = arrays.Array(size)
    value = min_value
    if max_diff == None:
        max_diff = 4
    for i in range(size):
        next_diff = random.randint(1, max_diff)
        value += next_diff
        an_array[i] = value
    return an_array

def cat(a,b):
    lenA=len(a)
    lenB=len(b)
    total=0
    array=arrays.Array(lenA+lenB)

    for i in range(lenA):
        array[i]=a[i]
        total+=1

    for i in range(lenB):
        array[total]=b[i]

    return array
