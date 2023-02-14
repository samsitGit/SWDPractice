import turtle
import pixart

def test_initialize():
    assert (-300, turtle.xcor())

def test_black_pixel():
    pixart.initialize()
    pixart.draw_black_pixel()
    assert (-270, turtle.xcor())
    assert (300, turtle.ycor())
    assert (False, turtle.isdown())
    assert ("black", turtle.pencolor())
    assert ("black", turtle.fillcolor())