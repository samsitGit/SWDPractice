'''
    4.2 Lecture
    Author: Sam Sit
'''

import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

def initialize():
    turtle.reset()
    turtle.bgcolor("blue")
    turtle.tracer(0)
    turtle.up()
    turtle.goto(-300, 300)
    turtle.pensize(1)
    turtle.fillcolor("white")
    turtle.pencolor("black")
    turtle.down()

def draw_black_pixel():
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.down()
    times = 0
    while times < 5:
        times = times + 1
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()
    #turtle.goto(0, 0)

def main():
    initialize()
    draw_black_pixel()
    input()

main()