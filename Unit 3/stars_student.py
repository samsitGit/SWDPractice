"""
Draws a sky filled with stars and planets.
HW3.2
@author Sam Sit
"""

import random
import turtle
STAR = 108
POINT = 36

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    '''
    Type of error: semantic
    Cause: misplaced parameter values
    Discovery: comes out non-yellow color
    '''
    turtle.fillcolor(red, green, blue)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    x = random.randint(-800, 800)
    '''
    Type of error: syntax
    Cause: lacks a comma
    Discovery: VSC crashed with a syntax error at this line
    '''
    y = random.randint(-500, 500)
    '''
    Type of error: semantic
    Cause: lacks pen up
    Discovery: lines follow the star
    '''
    turtle.up()
    '''
    Type of error: semantic
    Cause: typo in second parameter 
    Discovery: stars appears in a straight line rather than scattered
    '''
    turtle.goto(x, y)

    '''
    Type of error: semantic
    Cause: angle is not used
    Discovery: all stars in same angle and angle is not used
    '''
    angle = random.randint(0, 360)
    turtle.left(angle)

    '''
    Type of error: syntax
    Cause: lacks a semicolon after function definition
    Discovery: VSC crashed with a syntax error at this line
    '''

def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()

    turtle.down()
    turtle.begin_fill()

    turtle.forward(length)
    turtle.left(POINT)
    turtle.forward(length)
    turtle.right(STAR)

    turtle.forward(length)
    turtle.left(POINT)
    turtle.forward(length)
    turtle.right(STAR)

    turtle.forward(length)
    turtle.left(POINT)
    turtle.forward(length)
    turtle.right(STAR)

    turtle.forward(length)
    turtle.left(POINT)
    turtle.forward(length)
    turtle.right(STAR)

    turtle.forward(length)
    turtle.left(POINT)
    turtle.forward(length)
    turtle.right(STAR)

    turtle.end_fill()    

def random_star():
    random_move()
    randomLength = random.randint(5, 10)
    draw_star(randomLength)

def draw_world(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_celestial_bodies():
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    draw_world(30, 40, 100, "red")
    draw_world(-20, -200, 20, "white")
    draw_world(-150, 60, 40, "orange")

def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    tweak(True, 1)
    '''
    Type of error: runtime
    Cause: input is a string and draw_star needs float
    Discovery: VSC crashed with a type error of not being able to multiply
    '''
    length = float(input("Enter length of star to draw (e.g. 100): "))
    draw_star(length)
    tweak(True, 0)
    draw_celestial_bodies()

    '''
    Type of error: runtime
    Cause: hide function doesn't exist
    Discovery: VSC crashed with an attribute error at this line
    '''
    turtle.hideturtle()
    input("Press enter to continue...")

main()