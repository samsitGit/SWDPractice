'''
    For fun
    Author: Sam Sit
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
    if index == 1 or index == 4:
        firstSide = 2
        secondSide = 3
    elif index == 3 or index == 2:
        firstSide = 1
        secondSide = 4
    array = change(array, index)
    array = change(array, firstSide)
    array = change(array, secondSide)

    return array

def solve(array):
    A = array[0]
    B = array[1]
    C = array[2]
    D = array[3]

def main():
    setup = [1, 2, 3, 4]
    target = [4, 4, 4, 4]
    solve(setup, target)

main()