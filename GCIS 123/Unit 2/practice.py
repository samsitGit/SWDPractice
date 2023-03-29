import turtle

def convert_height():
    height = int(input("Enter your height in inches: "))
    feet = str((height-1)//12)
    inch = str(height%12)
    print("You are", feet + "'", inch + "\"", "tall")

def convert_distance(km):
    inches = float(km*39370.1)
    miles = int(inches//63360)
    feet = int((inches%63360)//12)
    finalInch = int(inches - (miles*63360) - (feet*12))
    print(km, "kilometers is", miles, "miles,", feet, "feet,", finalInch, "inches")

def snow_man(x, y, radius):
    turtle.bgcolor("cyan")
    circle(x, y, radius)
    circle(x, (y+(2*radius)), .75*radius)
    circle(x, (y+(2*radius)+(2*.75*radius)), .75*.75*radius)

def circle(x, y, radius):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.circle(radius)
    turtle.end_fill()

def main():
    convert_height()
    convert_distance(123.5)
    convert_distance(60)
    convert_distance(96.56061)
    distance = float(input("Enter a number in kilometers to be converted: "))
    convert_distance(distance)
    snow_man(0, -200, 100)
    input("Press enter to continue...")

main()