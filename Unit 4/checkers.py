'''
    4.2 HW
    Author: Sam Sit
'''

import turtle
import pixart

def draw_checkers():
    totalRows = 20
    count = 0
    while count < totalRows:
        draw_checkers_row(count, 20)
        count = count + 1


def draw_checkers_row(row, col):
    count = 0
    rowY = 300 - (row * pixart.PIXEL_SIZE)
    turtle.goto(-300, rowY)
    while count < col/2:
        if row % 2 == 0:
            pixart.draw_pixel_by_code(2)
            pixart.draw_pixel_by_code(0)
        else:
            pixart.draw_pixel_by_code(0)
            pixart.draw_pixel_by_code(2)
        count = count + 1

def main():
    pixart.initialize()
    #turtle.tracer(0)
    draw_checkers()
    input()

main()