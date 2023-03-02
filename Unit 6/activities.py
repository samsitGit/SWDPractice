'''
    6.1-6, 6.10 lecture

    Author: Sam Sit
'''
import arrays
import random
import time
import searches
import arrays_utils

def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1,0))
    print(arrays.Array(10,""))
    print(arrays.Array(20, False))

def while_fill(an_array):
    i = 0
    while i < len(an_array):
        an_array[i] = i
        i += 1
    print(an_array)

def for_fill(an_array):
    count = 0
    for i in range(len(an_array)):
        an_array[i] = count
        count += 1
    print(an_array)

def roll_the_die(sides):
    number = random.randint(1, int(sides))
    print("rolling a " + str(sides) + "-sided die: " + str(number))

def linear_search_timer(an_array, target):
    begin = time.perf_counter()
        
    searches.linear_search(an_array, target)

    end = time.perf_counter()
    elapsed = end - begin
    print("elapsed time:", elapsed)

def main():

    #making_arrays()
    '''
    an_array = arrays.Array(10)
    print(an_array)
    while_fill(an_array)
    for_fill(an_array)

    random.seed(1)

    for i in range(10):
        roll_the_die(6)
    '''
    array = arrays_utils.range_array(1,100)
    target = 50
    linear_search_timer(array, target)

main()