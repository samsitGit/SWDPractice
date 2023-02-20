'''
    4.2 + 4.3 Lecture
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

def printSepLine(string):
    print(string)
    count = 0
    while count < 4:
        print(string[count])
        count = count + 1

def printSepLineReverse(string):
    print(string)
    count = 3
    while count >= 0:
        print(string[count])
        count = count - 1

def loopSpam():
    sum = 0
    while True:
        num = int(input())
        if num == 0:
            break
        elif num % 2 == 0:
            continue
        else:
            sum = sum + num
    print("sum = " + str(sum))

def print_range(range):
    for char in range:
        print(char, end=" ")
    print()

def print_reverse(string):
    newString = ""
    for char in string:
        newString = char + newString
    print(newString)

def splitString(string, delimiter):
    if delimiter == "" or delimiter == None:
        for i in string:
            print(i)
    else:
        tokens = string.split(delimiter)
        for i in tokens:
            print(i)

def main():
    #countdown(5)
    #quotable()
    #printSepLine("Yoda")
    #printSepLineReverse("Yoda")
    #loopSpam()
    #r1_5 = range(1, 5)
    #print_range(r1_5)
    #r2_10 = range(2, 10)
    #print_range(r2_10)
    #print_reverse("")
    #print_reverse("a")
    #print_reverse("Hello, World!")
    #print_reverse("Sam Sit")
    #delimiter = '\n'
    #splitString('"That\'s my house," I said.', delimiter)
    #splitString("one two,\tthree\nfour five", delimiter)
    #splitString("My name is \"Lucy van Pelt.\"", delimiter)

main()