import random

def is_correct(guess, answer):
    return guess == answer
def main():
    answer = random.randint(1,10)
    guess = input("Guess a number between 1-10: ")
    print(is_correct(guess, answer))

main()