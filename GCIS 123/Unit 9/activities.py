'''
    9 lecture
    Author: Sam Sit
'''

import arrays
import timing

def unique_array(a, v):
    for i in range(len(a)):
        if a[i] == None:
            a[i] = v
            break
        elif a[i] == v:
            return

def fill_array(l):
    a = arrays.Array(l)
    for i in range(l-1):
        unique_array(a, i)

def main():
    timing.time_function(fill_array, 5000)

main()