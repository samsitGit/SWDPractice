def convert_height():
    height = int(input("Enter your height in inches: "))
    feet = str((height-1)//12)
    inch = str(height%12)
    print("You are", feet + "'", inch + "\"", "tall")

def convert_distance(km):
    inches = km*39370.1
    miles = int(inches//63360)
    feet = int((inches%63360)//12)
    finalInch = int(inches - (miles*63360) - (feet*12))
    print(km, "kilometers is", miles, "miles,", feet, "feet,", finalInch, "inches")

def main():
    #convert_height()
    convert_distance(123.5)
    convert_distance(60)
    convert_distance(96.56061)

main()