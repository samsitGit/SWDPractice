'''
    4.2 Lecture
    Author: Sam Sit
'''

def countdown(number):
    sum = 0
    while number > 0:
        print(number)
        sum = sum + number
        number = number - 1
    print("sum: " + str(sum))

def main():
    countdown(5)

main()