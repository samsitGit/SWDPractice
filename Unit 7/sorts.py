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

def main():
    array = array_utils.range_array(1,10)
    print(swap(array, 0, 5))

main()