'''
    4.1 Powerpoint
    Author: Sam Sit
    Must run "python -m pytest"
'''

import random

def is_correct(guess, answer):
    #return guess == answer
    if guess == answer:
        print("You guessed the number!")
    
    else:
        print("Your guess was", int(check_guess(guess, answer)), "away from the number.")

def isEquilateral (a, b, c):
    if a == b and b == c and c == a:
        print("Yes")
    else:
        print("No")

def check_guess(guess, answer):
    if guess == answer:
        return 0
    else:
        difference = ((guess - answer)**2)**.5
        return difference

def test_check_guess_correct():
    assert check_guess(5, 5) == 0

#def test_check_guess_incorrect():
#    assert (check_guess(4, 5)) > 0
#    assert (check_guess(5, 4)) > 0

def test_check_guess_too_high():
    assert (check_guess(5, 4)) > 0

def test_check_guess_too_low():
    assert (check_guess(4, 5)) > 0

def main():
    answer = random.randint(1,10)
    guess = int(input("Guess a number between 1-10: "))
    #print(is_correct(guess, answer))
    is_correct(guess, answer)

main()