def variable_practice():
    ageInMonths = int(268)
    numberOfDaysInAYear = int(365)
    nameOfFirstPet = str("Maple")
    first5DigitsOfPi = int(14159)
    print(ageInMonths, numberOfDaysInAYear, nameOfFirstPet, first5DigitsOfPi)

def expressions_practice():
    literal = 5
    addition = 5+2
    exponent = 5**2
    floorDivision = 5/2
    mod = 5%2
    para = (5+2)*2
    mix = (5**2*2+2)/2
    print(literal, addition, exponent, floorDivision, mod, para, mix)

#asks users for two numbers and print the results of operations
def prompt_and_print():
    num1 = float(input("first number: "))
    num2 = float(input("second number: "))
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)

def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()

main()