'''
    Practice for functions in HW 2.2
    Author: Sam Sit
'''

def ageInMonths():
    currentYear = int(input("Current year: "))
    currentMonth = int(input("Current month: "))
    birthYear = int(input("Birth year: "))
    birthMonth = int(input("Birth month: "))

    print(((currentYear-birthYear)*12)+(currentMonth-birthMonth))

def dayOfYear():
    currentMonth = float(input("Enter the month: "))
    currentDay = float(input("Enter the day of the month: "))
    
    print("The approximate day of the year is: ", ((currentMonth-1)*30.4+currentDay))

def main():
    ageInMonths()
    dayOfYear()


main()