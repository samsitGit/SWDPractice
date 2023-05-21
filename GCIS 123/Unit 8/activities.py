'''
    8.2-3 Lecture
    Author: Sam Sit
'''

import arrays
import array_utils

def tuples(a_tuple):
    print(len(a_tuple))
    #a_tuple[0] = "b" #wont work
    for i in a_tuple:
        print(i)

def lists():
    list1 = [5, 2, "a", True]
    list1[0] = 1 #works
    for i in list1:
        print(i)
    print(list1)
    #skip 8.4

def make_list(a_sequence):
    list = []
    for i in a_sequence:
        list.append(i)
    return list

def scale(a_list, scalar):
    for i in range(len(a_list)):
        a_list[i] *= scalar
    return a_list

def mutater(a_list, an_int):
    print(a_list)
    print(an_int)
    an_int*=5
    a_list[0]*=5
    print(a_list)
    print(an_int)

def cat(a, b):
    c = a+b
    return c

def extender(a, b):
    a+=b
    return a

def inserter(a, v):
    i = int(len(a)/2)
    a.insert(i, v)
    return a

def popper(a):
    for i in range(len(a)):
        a.pop(0)
        print(a)

def array_insert(a, i, v):
    a1 = arrays.Array(len(a)+1)
    over = False
    for j in range(len(a)+1):
        if j == i:
            a1[j] = v
            over = True
        elif over:
            a1[j] = a[j-1]
        else:
            a1[j] = a[j]
    
    return a1

def array_pop(a, i):
    a1 = arrays.Array(len(a)-1)
    over = False
    for j in range(len(a)):
        if j == i:
            over = True
        elif over:
            a1[j-1] = a[j]
        else:
            a1[j] = a[j]
    
    return a1

def main():
    x = ("a", 123, False)
    y = tuple("abcd")

    tuples(x)
    tuples(y)

    lists()

    print(make_list("test"))
    print(scale(make_list((5, 20, 2, 4)), 2))
    mutater(make_list((2,4,5)),6)

    a = make_list("abc")
    b = make_list("de")
    print(a)
    print(b)
    print(cat(a,b))

    a = make_list("abc")
    b = make_list("de")
    print(a)
    print(b)
    print(extender(a,b))

    a=[]
    print(inserter(a, 0))
    print(inserter(a, 1))
    print(inserter(a, 2))
    print(inserter(a, 3))
    print(inserter(a, 4))

    popper(a)

    a = array_utils.range_array(0, 10)
    print(a)
    a = array_insert(a, 4, 99)
    print(a)
    print(array_pop(a, 7))

main()