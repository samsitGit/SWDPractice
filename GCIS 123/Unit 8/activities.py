'''
    8 Lecture
    Author: Sam Sit
'''

import arrays
import array_utils
import random

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

def rgb_tuple():
    r = random.random()
    g = random.random()
    b = random.random()
    
    return (r,g,b)

def tuple_equality(a, b):
    print(a)
    print(b)
    print(a is b)
    print(a == b)

def reverse_sequence(a):
    b = []

    for i in range(len(a)):
        b.append(a[len(a)-i-1])
    
    return b

def slices():
    a = "Somebody once told me the world was gonna roll me."
    b = list(a)
    s = 0
    e = 0
    for i in range(len(b)):
        s = e
        if b[i] == " ":
            e = i
            print(b[s:e])
            e += 1
        elif i == len(b)-1:
            e = i
            print(b[s:e])

#instructions in clear
def dices(a):
    if len(a) == 0:
        return False
    else:
        e = a[0:1]
        print(e)
        dices(a[1:])      

def random_list(s):
    l = []
    for i in range(s):
        l.append(random.randint(0, 100))
    return l

def sorted_test(a, b=False):
    print(a)
    b = sorted(a, reverse=b)
    print(b)

def sort_test(a, b=False):
    print(a)
    a.sort(reverse=b)
    print(a)

def sort_cards(h):
    print(h)
    h.sort(key=suit_key)
    print(h)

def suit_key(c):
    key = 0
    suit = c[1]
    if suit == "C":
        key = 1
    elif suit == "D":
        key = 2
    elif suit == "H":
        key = 3
    else:
        key = 4
    return key

def packer():
    return 1, 2, 3, 4

def swapper(a):
    b = []
    c = len(a)
    d = int(c/2)
    for i in range(d,c):
        b.append(a[i])
    for i in range(d):
        b.append(a[i])
    return b

def chunky(a, s):
    for i in range(int(len(a)/s)+1):
        c = a[i*s:i*s+s]
        print(c)

def sevens_key(n):
    if str(n)[0] == "7":
        return 0
    else:
        return 1
    
def lucky_7s(a):
    print(a)
    a.sort(key=sevens_key)
    print(a)

def comprehension():
    print([x for x in "foobar"])
    print([0 for x in range(15)])
    print([x for x in range(13)])
    print([x for x in range(0, 20, 2)])
    print([x for x in range(0, 50) if not x % 3 or not x % 5])

def main():
    '''
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
    
    print(rgb_tuple())
    print(rgb_tuple())
    print(rgb_tuple())
    
    a = ["a", 12, True]
    b = tuple(a)
    c = tuple(a)
    d = tuple([12, True, "a"])
    tuple_equality(a,b)
    tuple_equality(b,c)
    tuple_equality(c,d)

    a = list("magic")
    print(reverse_sequence(a))
    
    slices()
    a = list("magic wand")
    dices(a)
    
    sorted_test(random_list(10))
    
    sort_test(random_list(10))
    
    a = random_list(10)
    sorted_test(a, True)
    sort_test(a, True)
    sorted_test(a, False)
    sort_test(a, False)
    
    hand = [(10, "D"), (10, "C"), (9, "H"), (6, "D"), (2, "S")]
    sort_cards(hand)
    
    hand = [(10, "D"), (10, "C"), (10, "H"), (10, "S")]
    sort_cards(hand)
    
    packed = packer()
    print(packed)
    a = packed[0]
    b = packed[1]
    c = packed[2]
    d = packed[3]
    print(a)
    print(b)
    print(c)
    print(d)
    
    a = []
    b = [1]
    c = [1,2,3]
    d = list("1234567890")
    print(swapper(a))
    print(swapper(b))
    print(swapper(c))
    print(swapper(d))
    
    d = list("1234567890")
    chunky(d, 3)
    
    a = array_utils.range_array(0, 100, 1)
    b = []
    for i in range(len(a)):
        b.append(a[i])
    lucky_7s(b)
    '''
    comprehension()
main()