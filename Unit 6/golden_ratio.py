'''
    6.1A The Golden Ratio HW

    Author: Sam Sit
'''

import arrays

#6.1
def fibonacci(n):
    n = int(n)
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

#6.2
def fill_fibonacci_array(array, index = 0):
    if index < len(array):
        array[index] = fibonacci(index+1)
        fill_fibonacci_array(array, index+1)
    return array

def main():

    #6.1
    n = 9
    print(fibonacci(n))

    #6.3
    size = 20
    array = arrays.Array(size)
    print(fill_fibonacci_array(array))
    



main()