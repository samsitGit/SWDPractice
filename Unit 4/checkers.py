'''
    4.2 HW
    Author: Sam Sit
'''

import turtle
import pixart

def draw_checkers():

    draw_checkers_row(1, 20)


def draw_checkers_row(row, col):
    count = 0
    turtle.goto(-300, row*pixart.PIXEL_SIZE)
    while count < col/2:
        pixart.draw_pixel_by_code(2)
        pixart.draw_pixel_by_code(0)
        count = count + 1

def main():
    pixart.initialize()
    draw_checkers()
    input()

main()