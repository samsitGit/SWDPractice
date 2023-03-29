'''
    6.1A The Golden Ratio HW

    Author: Sam Sit
'''

import arrays
import turtle
import random

#6.1.1
def fibonacci(n):
    n = int(n)
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

#6.1.2
def fill_fibonacci_array(array, index = 0):
    if index < len(array):
        array[index] = fibonacci(index+1)
        fill_fibonacci_array(array, index+1)
    return array

#6.1.4
def print_ratios(array, index = 0):
    a = array[index]
    b = array[index+1]

    if index < (len(array)-2):

        try:
            print(f"{a:>4n} {b:>4n}  {(b/a):.5f}  {((a+b)/b):.5f}")
            
        except:
            print(f"{a:>4n} {b:>4n}  undefined")

        print_ratios(array, index+1)

#6.1.6
def draw_fibonacci_spiral():
    size = 15
    scale = 2
    #can do size = 12, scale = 5
    array = fill_fibonacci_array(arrays.Array(size))

    #turtle.tracer(0)
    initialize()
    squares(array, size, scale)
    initialize()
    turtle.right(90)
    circles(array, size, scale)

def initialize():
    turtle.setheading(0)
    turtle.colormode(255)
    turtle.up()
    turtle.goto(-800, -500)
    turtle.down()

def squares(array, depth, scale):
    if depth > 1:
        square(array[depth-1], random_color(), scale)
        squares(array, depth-1, scale)

def square(size, color, scale):
    size *= scale
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    turtle.up()
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.down()

def circles(array, depth, scale):
    if depth > 1:
        circle(array[depth-1], scale)
        circles(array, depth-1, scale)

def circle(size, scale):
    size *= scale
    turtle.pensize(3)
    turtle.circle(size, -90)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def main():
    '''
    #6.1.1
    n = 9
    #print(fibonacci(n))

    #6.1.3
    size = 20
    array = arrays.Array(size)
    print(fill_fibonacci_array(array))
    
    #6.1.5
    size = 21
    array = arrays.Array(size)
    print_ratios(fill_fibonacci_array(array))
    '''

    #6.1.6
    draw_fibonacci_spiral()
    input()

main()