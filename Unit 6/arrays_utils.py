'''
    6.7 lecture

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

def main():
    
    random.seed(1)

    print(random_array(10))


main()