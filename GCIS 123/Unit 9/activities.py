'''
    9 lecture
    Author: Sam Sit
'''

import arrays
import timing
import random

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

def coupon_collector(n):
    collection = set()
    count = 0
    while len(collection) < n:
        draw = random.randint(1, n)
        collection.add(draw)
        count += 1
    return count

def mixup():
    a = set("characters")
    for i in a:
        print(i, end = " ")

def unique_words(fn):
    words = set()
    with open(fn) as f:
        next(f)
        for word in f:
            word = word.lower()
            words.add(word)
    return len(words)

def superset(a, b):
    c = 0
    for i in b:
        if i in a:
            c += 1
    if c == len(b):
        return True
    else:
        return False

def subset(b, a):
    c = 0
    for i in b:
        if i in a:
            c += 1
    if c == len(b):
        return True
    else:
        return False

def intersection(a, b):
    c = set()
    for i in a:
        if i in b:
            c.add(i)
    return c

def union(a, b):
    c = b
    for i in a:
        c.add(i)
    return c

def minus(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    return a

def names():
    a = dict()
    a["S"] = "Sam"
    a["A"] = "Alden"
    a["Si"] = "Sit"

    if "S" in a:
        print(a["S"])

    return a

def print_dict(dict):
    for key in dict:
        v = dict[key]
        print(key, ":", v)

def count_words(filename):
    result = dict()
    with open(filename) as file:
        for line in file:
            line = line.lower()
            words = line.split()
            for word in words:
                if word[-1] == "." or word[-1] == ",":
                    word = word[:-1]
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    sorted_results = sorted(result.items(), key=lambda x:x[1])
    return sorted_results

def numbers():
    a = dict()
    a["S"] = 5
    a["A"] = 2
    a["Si"] = 3

    return a

def find_max(dict):
    max = 0
    high_key = ""
    for key in dict:
        v = dict[key]
        if v > max:
            max = v
            high_key = key
    return high_key + ":" + str(max)
           
def main():
    '''
    timing.time_function(fill_array, 5000)
    
    timing.time_function(fill_list, 5000)
    
    sets()
    
    timing.time_function(fill_set, 5000)
    
    print(coupon_collector(10000))
    
    mixup()
    
    print(unique_words("data/alice.txt"))
    
    a = set("abc")
    b = set("bc")
    print(superset(a, b))
    a = set("abc")
    b = set("bce")
    print(superset(a, b))
    
    a = set("abc")
    b = set("abcd")
    print(subset(a, b))
    a = set("abc")
    b = set("bce")
    print(subset(a, b))
    
    a = set("a1bc")
    b = set("abcd1")
    print(intersection(a, b))
    
    a = set("a14234bc")
    b = set("abc2d1")
    print(a)
    print(minus(a, b))
    
    print(names())
    
    print_dict(names())
    
    result = count_words("data/alice.txt")
    for i in result:
        print (i)
    '''
    
    print(find_max(numbers()))

main()