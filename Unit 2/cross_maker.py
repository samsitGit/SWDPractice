'''
    4.3 HW
    Author: Sam Sit
'''

import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

#def cross_maker():

def initialize():
    turtle.reset()
    turtle.bgcolor("gray")
    turtle.speed(0)
    turtle.up()
    turtle.goto(-300, 300)
    turtle.pensize(1)
    turtle.fillcolor("white")
    turtle.pencolor("black")

def write_letter(letter):
    turtle.write(letter, align='center', font=("Arial", 19, "normal"))


def move(col, row):
    turtle.goto(-300 + col * PIXEL_SIZE, 300 - row * PIXEL_SIZE)

def main():
    initialize()
    move(4,5)
    write_letter("B")
    input()

main()