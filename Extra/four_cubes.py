'''
    Spring Break Genshin Impact Puzzle Fun
    Authors: Sam Sit, Edward Riley
'''

import random, copy

'''
    +----+----+
    | A0 | B1 |
    +----+----+
    | C2 | D3 | 
    +----+----+
'''

'''
    +----+----+
    | A1 | B2 |
    +----+----+
    | C3 | D4 | 
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

def random_solve(array, target):
    attempts = 0
    moves = []
    
    while not array == target:
        randInt = random.randint(0, 3)
        hit(array, randInt)
        moves.append(randInt)
        attempts +=1
        
    return attempts, moves, array

def brute_solve(array, target):

    lowestAttempt = 15
    fastestMoves = []

    for i in range(500):
        setup = copy.deepcopy(array) # either this or hardcode setup here
        attempts, moves, final_arr = random_solve(setup, target)
        
        if attempts < lowestAttempt:
            epoch = i
            lowestAttempt = attempts
            fastestMoves = moves

    if fastestMoves:
        print(f"Few attempts! {lowestAttempt} The moves were {fastestMoves}. Found at the Epoch {epoch}.")
    else:
        print('Failed.')

def main():
    target = [4, 4, 4, 4]
    setup = [4, 2, 2, 4]
    brute_solve(setup, target)


main()