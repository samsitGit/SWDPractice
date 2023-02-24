'''
    5.11-19 lecture
    command while in unit5: python activities.py

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
        except FileNotFoundError:
            print("File does not exist:", filename)
        #except ValueError:
        #    print("File contains non-numeric data")
    print("Total sum:", totalSum)

def sum(filename):
    sum = 0
    with open(filename) as file:
        for line in file:
            try:
                sum += int(line)
            except ValueError:
                print("Skipping non-numeric data:", line.strip())
    return sum

def division():
    numAttempts = 3
    while True:
        try:
            num = input("Enter a numerator: ")
            if num == "":
                break
            num = float(num)
            den = input("Enter a denominator: ")
            if den == "":
                break
            den = float(den)
            print(num/den)
        except ZeroDivisionError:
            print("Can't divide by 0.")
        except ValueError as ve:
            numAttempts -= 1
            if numAttempts > 0:
                print("Invalid.", numAttempts, "attempts remaining")
            else:
                raise ve
#            print("Non-numeric value entered.")
            
def password():
    password = input("Enter password: ")
    if len(password)>20 or len(password)<10:
        raise ValueError("Password must be in between 10 and 20 characters.")
    confirmPass = input("Confirm password: ")
    if password != confirmPass:
        raise ValueError("Passwords must match!")

def exponent(base, power):
    if power < 0:
        raise ValueError("Power must not be negative: " + str(power))
    originalBase = base
    for i in range(power-1):
        base = base * originalBase
    print(base)
    return(base)

def main():
    #numbers()
    #division()
    #password()
    #exponent(5, 3)
    #exponent(2, 4)
    #exponent(3, 3)
    #exponent(3, -1)
    print()

main()