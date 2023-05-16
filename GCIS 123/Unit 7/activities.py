'''
    7.8 Lecture
    Author: Sam Sit
'''

import array_utils

def evens(n):
    n += 1 #move index up
    sum = 0
    for i in range(n):
        if not i % 2: #even numbers only
            sum += i
    return sum


def main():
    print(evens(100))

main()