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
    #assuming turtle return to original place
    assertle(-300, 300, False, "black", "green")

def test_write_letter():
    cross_maker.initialize()
    turtle.speed(5)
    cross_maker.write_letter("b")
    #turtle wont return to original place because there is no need to
    #simply use move function to move around
    #angle is still in the right place
    assertle(-285, 270, False, "black", "green")
    input()

def test_write_word():
    cross_maker.initialize()
    cross_maker.write_word(3, 6, "everyone", "h")
    assertle(15, 90, False, "black", "green")
    input()

def assertle(x, y, state, pen, fill):
    assert (x == round(turtle.xcor()))
    assert (y == round(turtle.ycor()))
    assert (state == turtle.isdown())
    assert (pen == turtle.pencolor())
    assert (fill == turtle.fillcolor())