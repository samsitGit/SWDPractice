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
    turtle.speed(0)
    turtle.up()
    turtle.goto(-300, 300)
    turtle.pensize(1)
    turtle.fillcolor("white")
    turtle.pencolor("black")

#def draw_black_pixel():
def draw_pixel(color):
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.down()
    times = 0
    while times < 4:
        times = times + 1
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
'''
def draw_red_pixel():
    turtle.pencolor("black")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.down()
    times = 0
    while times < 4:
        times = times + 1
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
'''
def main():
    initialize()
    input()

main()