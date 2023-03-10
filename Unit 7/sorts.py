'''
    7.2 Lecture
    Author: Sam Sit
'''

import array_utils
def swap(an_array, a, b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp
    return an_array

def shift(an_array, index):
    for i in range(index):
        if an_array[index-i] < an_array[index-i-1]:
            swap(an_array, index-i, index-i-1)
        else:
            break
    return an_array

def main():
    array = array_utils.range_array(1,10)
    print(array)
    #print(swap(array, 0, 5))
    result = swap(array, 0, 5)
    print(result)
    print(shift(result, 5))

main()