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

def write_letter(letter):
    draw_pixel("green")
    turtle.right(90)
    turtle.forward(PIXEL_SIZE)
    turtle.left(90)
    turtle.forward(PIXEL_SIZE/2)
    turtle.write(letter, align='center', font=("Arial", 19, "normal"))

def write_word(col, row, word, axis):
    if axis == "h":
        count = 0
        for i in range(len(word)):
            move(col+count, row)
            count += 1
            write_letter(word[i])
    elif axis == "v":
        count = 0
        for i in range(len(word)):
            move(col, row+count)
            count += 1
            write_letter(word[i])

def decode_command(string):
    tokens = string.split(" ")
    col = int(tokens[0])
    row = int(tokens[1])
    word = tokens[2]
    axis = tokens[3]
    write_word(col, row, word, axis)

def move(col, row):
    turtle.goto(-300 + col * PIXEL_SIZE, 300 - row * PIXEL_SIZE)

def user_menu():
    while True:
        command = input("Enter a command: ")
        if command == "" or command == None:
            break
        else:
            decode_command(command)

def main():
    initialize()
    #move(4,5)
    #write_letter("B")
    #write_word(3, 6, "everyone", "h")
    #command = input("Enter a command: ")
    #decode_command(command)
    user_menu()
    #input()

main()