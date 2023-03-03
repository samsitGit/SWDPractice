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

#6.4
def print_ratios(array, index = 0):
    a = array[index]
    b = array[index+1]

    if index < (len(array)-2):

        try:
            print(f"{a:>4n} {b:>4n}  {(b/a):.5f}  {((a+b)/b):.5f}")
            
        except:
            print(f"{a:>4n} {b:>4n}  undefined")

        print_ratios(array, index+1)

def main():
    '''
    #6.1
    n = 9
    #print(fibonacci(n))

    #6.3
    size = 20
    array = arrays.Array(size)
    print(fill_fibonacci_array(array))
    '''

    #6.4
    size = 21
    array = arrays.Array(size)
    print_ratios(fill_fibonacci_array(array))


main()