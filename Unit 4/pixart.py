'''
    4.2 Lecture
    Author: Sam Sit
'''

import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def initialize(x, y, side):
    turtle.bgcolor("blue")
    turtle.tracer(0)
    turtle.up()
    turtle.goto(x, y)
    turtle.pensize(1)
    turtle.fillcolor("white")
    turtle.pencolor("black")
    turtle.down()


def main():
    initialize(-300, 300, 100)

main()