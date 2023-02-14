'''
    4.2 Lecture & HW
    Author: Sam Sit
'''

import turtle
import pixart
import checkers

def test_initialize():
    pixart.initialize()
#    assert (-300 == turtle.xcor())
    assertle(0, -300, 300, False, "black", "white")

def test_black_pixel():
    #pixart.draw_black_pixel()
    pixart.draw_pixel("black")
    assertle(0, -270, 300, False, "black", "black")

def test_red_pixel():
    #pixart.draw_red_pixel()
    pixart.draw_pixel("red")
    assertle(0, -240, 300, False, "black", "red")

def test_pixel_by_code():
    pixart.draw_pixel_by_code(5)
    assertle(0, -210, 300, False, "black", "green")

def test_checkers():
    pixart.initialize()
    checkers.draw_checkers()
    assertle(0, 300, 300, False, "black", "black")
    

#def test_checkers_row():
    #checkers.draw_checkers_row(1, 20)

def assertle(speed, x, y, state, pen, fill):
    assert (speed == turtle.speed())
    assert (x == round(turtle.xcor()))
    assert (y == round(turtle.ycor()))
    assert (state == turtle.isdown())
    assert (pen == turtle.pencolor())
    assert (fill == turtle.fillcolor())
