'''
    4.3 HW
    Author: Sam Sit
    python -m pytest -s .\pixart_test.py::test_checkers
'''

import turtle
import cross_maker

def test_draw_pixel():
    cross_maker.initialize()
    cross_maker.draw_pixel("green")
    assertle(0, -300, 300, False, "black", "green")


def assertle(speed, x, y, state, pen, fill):
    assert (speed == turtle.speed())
    assert (x == round(turtle.xcor()))
    assert (y == round(turtle.ycor()))
    assert (state == turtle.isdown())
    assert (pen == turtle.pencolor())
    assert (fill == turtle.fillcolor())