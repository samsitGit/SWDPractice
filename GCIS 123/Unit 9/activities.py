'''
    9 lecture
    Author: Sam Sit
'''

import arrays
import timing

def unique_array(a, v):
    noneIndex = None
    noneIndexFound = False
    for i in range(len(a)):
        if a[i] == None and not noneIndexFound:
            noneIndex = i
            noneIndexFound = True
        elif a[i] == v:
            return
    a[noneIndex] = v

def fill_array(l):
    a = arrays.Array(l)
    for i in range(l-1):
        unique_array(a, i)

def unique_list(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return
    a.append(v)

def fill_list(l):
    e = []
    for i in range(l-1):
        unique_list(e, i)

def sets():
    a = {111, 3, 57}
    print(a)
    a.add(5)
    a.add(4)
    print(a)
    b = set("abbcdefg")
    print(b)

def unique_set(a, v):
    if v not in a:
        a.add(v)

def fill_set(l):
    s = set()
    for i in range(l-1):
        unique_set(s, i)

def main():
    '''
    timing.time_function(fill_array, 5000)
    
    timing.time_function(fill_list, 5000)
    
    sets()
    '''
    timing.time_function(fill_set, 5000)

main()