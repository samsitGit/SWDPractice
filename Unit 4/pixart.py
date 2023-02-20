'''
    4.2 Lecture + HW
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

def decoder(code):
    if code == "0":
        return "black"
    elif code == "1":
        return "white"
    elif code == "2":
        return "red"
    elif code == "3":
        return "yellow"
    elif code == "4":
        return "orange"
    elif code == "5":
        return "green"
    elif code == "6":
        return "yellowgreen"
    elif code == "7":
        return "sienna"
    elif code == "8":
        return "tan"
    elif code == "9":
        return "gray"
    elif code == 'A':
        return "darkgray"
    else:
        return False
    
def draw_pixel_by_code(code):
    turtle.pencolor("black")
    turtle.fillcolor(decoder(code))
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

def next_row():
    rowY = turtle.ycor()
    turtle.goto(-300, rowY - PIXEL_SIZE)

def move(col, row):
    turtle.goto(-300 + col * PIXEL_SIZE, 300 - row * PIXEL_SIZE)

def draw_row(row, col, num, color):
    #5 4 8
    count = 0
    #color = "red"

    while count < num:
        #4 + 0
        move(col + count, row)
        draw_pixel(color)
        count += 1

def square(row, column, size, color):
    for i in range(size):
        draw_row(row+i, column, size, color)

def rectangle(row, column, height, width, color):
    for i in range(height):
        draw_row(row+i, column, width, color)

def main():
    initialize()
    #draw_row(5, 4, 8, "red")
    turtle.tracer(0)
    #square(4, 5, 8, "green")
    rectangle(4, 5, 6, 10, "orange")
    input()

main()