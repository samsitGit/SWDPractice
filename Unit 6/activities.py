'''
    6.1-6 lecture

    Author: Sam Sit
'''
import arrays
import random

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

def main():

    #making_arrays()

    an_array = arrays.Array(10)
    print(an_array)
    while_fill(an_array)
    for_fill(an_array)

    random.seed(1)

    for i in range(10):
        roll_the_die(6)

main()