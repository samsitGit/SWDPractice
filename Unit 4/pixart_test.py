import turtle
import pixart

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

def assertle(speed, x, y, state, pen, fill):
    assert (speed == turtle.speed())
    assert (x == turtle.xcor())
    assert (y == turtle.ycor())
    assert (state == turtle.isdown())
    assert (pen == turtle.pencolor())
    assert (fill == turtle.fillcolor())
