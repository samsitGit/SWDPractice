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

def quotable():
    print("She said \"I don't like broccoli\".")
    print("A\tB\tC\tD\tE")
    print("This/is\\a/test\\.")
    print("This\nis a string\nwith newlines in\nthe middle.")
    print("She\t\tsaid \"I \\\ndon't\t\tlike \\\nbroccoli.\"")


def main():
    countdown(5)
    quotable()

main()