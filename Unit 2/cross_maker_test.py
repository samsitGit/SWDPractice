'''
    4.3 HW
    Author: Sam Sit
'''

import turtle
import cross_maker

def assertle(speed, x, y, state, pen, fill):
    assert (speed == turtle.speed())
    assert (x == round(turtle.xcor()))
    assert (y == round(turtle.ycor()))
    assert (state == turtle.isdown())
    assert (pen == turtle.pencolor())
    assert (fill == turtle.fillcolor())