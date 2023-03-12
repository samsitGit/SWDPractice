'''
    For fun
    Author: Sam Sit
'''

import random

'''
    +----+----+
    | A0 | B1 |
    +----+----+
    | C2 | D3 | 
    +----+----+
'''

def change(array, index):
    if array[index] == 4:
        array[index] = 1
    else:
        array[index] += 1
    return array

def hit(array, index):
    firstSide = 0
    secondSide = 0
    if index == 0 or index == 3:
        firstSide = 1
        secondSide = 2
    elif index == 1 or index == 2:
        firstSide = 0
        secondSide = 3
    array = change(array, index)
    array = change(array, firstSide)
    array = change(array, secondSide)

    return array

def edward_hypothesis_solve():
    
    print()
    

def solve(array, target):
    attempts = 0
    while True:
        randInt = random.randint(0, 3)
        
        hit(array, randInt)
        attempts +=1

        if array == target:
            return ("Success!", "Took this many attempts:", attempts

def main():
    setup = [1, 2, 3, 4]
    target = [4, 4, 4, 4]
    print(solve(setup, target))

main()