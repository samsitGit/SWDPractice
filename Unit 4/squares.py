'''
    4.1 HW
    Author: Sam Sit
'''

import turtle

def centeredSquare(x, y, side, color):
    half = side/2
    turtle.up()
    turtle.goto(x,y)
    turtle.pensize(4)
    turtle.color("black")
    turtle.fillcolor(color)
    turtle.forward(half)
    turtle.left(90)
    turtle.forward(half)
    turtle.begin_fill()
    turtle.down()
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()

def downSize(initalSide):
    a = initalSide / 2
    newSide = (a**2+a**2)**.5
    return newSide

def draw_squares(side):
    centeredSquare(0, 0, side, "red")
    turtle.left(45)
    side = downSize(side)
    centeredSquare(0, 0, side, "orange")
    turtle.left(45)
    side = downSize(side)
    centeredSquare(0, 0, side, "yellow")
    turtle.left(45)
    side = downSize(side)
    centeredSquare(0, 0, side, "green")
    turtle.left(45)
    side = downSize(side)
    centeredSquare(0, 0, side, "blue")
    turtle.left(45)
    side = downSize(side)
    centeredSquare(0, 0, side, "purple")

def main():
    turtle.tracer(0)
    draw_squares(750)
    turtle.hideturtle()
    input("Press enter to continue...")

main()