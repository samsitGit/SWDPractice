'''
    6.1-2 lecture

    Author: Sam Sit
'''
import arrays

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

def main():

    #making_arrays()

    an_array = arrays.Array(10)
    print(an_array)
    while_fill(an_array)


main()