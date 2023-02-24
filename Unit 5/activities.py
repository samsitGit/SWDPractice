'''
    5.11-12 lecture
    command while in unit5: python files.py

    Author: Sam Sit
'''

def numbers():
    filename = "init"
    #challenge
    totalSum = 0
    while True:
        filename = input("Enter filename: ")
        if filename == "":
            break
        try:
            result = sum(filename)
            print("Sum of numbers:", result)
            totalSum += result
        except:
            print("File does not exist:", filename)
    print("Total sum:", totalSum)

def sum(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            sum += int(line)
    return sum

def main():
    numbers()

main()