import turtle
import pixart

def test_initialize():
    assert (-300, turtle.xcor())

def test_black_pixel():
    pixart.initialize()
    pixart.draw_black_pixel()