'''
    6.9, 6.21-22 lecture

    Author: Sam Sit
'''
import arrays
import arrays_utils

def linear_search(an_array, target):
    count = 0
    for i in range(len(an_array)):
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

def main():
    array = arrays_utils.range_array(1,100)
    target = 50
    #print(linear_search(array, target))
    
    print(binary_search(array, target))
    print()

main()