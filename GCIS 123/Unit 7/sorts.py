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

def insertion_sort(an_array):
    for i in range(len(an_array)):
        shift(an_array, i)
    return an_array

def shift_wo_swap(an_array, index):
    target = an_array[index]
    target_index = index

    for i in range(1, index+1):
        if target < an_array[index-i]:
            swap(an_array, index-i, target_index)
            target_index -= 1

        else:
            break
    
    return an_array

def insertion_sort_wo_swap(an_array):
    for i in range(len(an_array)):
        shift_wo_swap(an_array, i)
    return an_array

def shiftOpposite(an_array, index):
    for i in range(index):
        if an_array[index-i] > an_array[index-i-1]:
            swap(an_array, index-i, index-i-1)
        else:
            break
    return an_array

def insertion_sort_reverse(an_array):
    for i in range(len(an_array)):
        shiftOpposite(an_array, i)
    return an_array

def main():
    #rray = array_utils.range_array(1,10)
    #print(array)
    #print(swap(array, 0, 5))
    #result = swap(array, 0, 5)
    #print(result)
    #print(shift(result, 5))

    #random = array_utils.random_array(10)
    #print(random)
    #print(insertion_sort(random))

    #new = [65, 79, 84, 86, 70, 63]
    #print(new)
    #print(shift_wo_swap(new, 4))

    random = array_utils.random_array(10)
    print("random size 10 array test")
    print(random)
    print(insertion_sort_wo_swap(random))

main()