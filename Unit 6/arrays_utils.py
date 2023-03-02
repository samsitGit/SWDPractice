'''
    6.7-8 lecture

    Author: Sam Sit
'''
import arrays
import random

def random_array(size, min_value=0, max_value=None):
    array = arrays.Array(size)
    count = 0
    if max_value == None:
        max_value = size
    for i in range(size):
        array[count] = random.randint(min_value, max_value)
        count += 1
    return array

def range_array(start, stop, step=1):
    stop += 1
    a_range = range(start, stop, step)
    a_array = arrays.Array(stop-start)
    count = 0
    for i in a_range:
        a_array[count] = i
        count += 1
    return a_array

def main():
    
    random.seed(1)

    #print(random_array(10))

    print(range_array(1, 10))


main()