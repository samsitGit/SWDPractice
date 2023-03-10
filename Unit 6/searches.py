'''
    6.9, 6.21-22 lecture

    Author: Sam Sit
'''
import arrays
import arrays_utils

def linear_search(an_array, target, start=None, end=None):
    
    length = len(an_array)

    if start == None or start < 0:
        start = 0
    
    if end == None or end > length:
        end = length
    
    count = start

    for i in range(start, end):
        if an_array[count] == target:
            print("found", target)
            return count
        count += 1
    print("did not find", target)
    return None

def binary_search(an_array, target, start=None, end=None):

    if start==None:
        start = 0
        end = len(an_array)

    midpoint = (start+end)//2
    mid = an_array[midpoint]
    
    if mid == target:    
        return midpoint
    elif mid < target:
        return binary_search(an_array, target, midpoint+1, end)
    elif mid > target:
        return binary_search(an_array, target, start, midpoint-1)

def jump_search(an_array, target):
    
    length = len(an_array)
    block_size = int(length**.5)
    count = 1

    for i in range(block_size):
        last_point = block_size * count - 1
        start_point = block_size * count - block_size
        last = an_array[last_point]
        if last == target:
            return last_point
        elif last > target:
            return linear_search(an_array, target, start_point, last_point)
        elif last < target:
            count += 1

    print("did not find", target)
    return None

def main():
    array = arrays_utils.range_array(1,100)
    target = 50
    #print(linear_search(array, target))
    
    #print(binary_search(array, target))
    print(jump_search(array, target))
    print()

main()