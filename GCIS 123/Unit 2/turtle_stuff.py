import turtle
angle = 90

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)

def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(), turtle.ycor())

def square(size, angle, pencolor, fillcolor):
    turtle.pensize(4)
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.home()
    turtle.end_fill()

def main():
    turtle_state()
    #test_drive()
    turtle.bgcolor("pink")
    square(150, 40, "blue", "red")
    square(100, 20, "green", "yellow")
    square(50, 60, "black", "purple")
    turtle_state()
    input("Press enter to continue...")

main()