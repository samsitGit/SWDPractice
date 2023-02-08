import turtle

def rect(x, y, height, base, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

def star(x, y, size, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.left(144)
    turtle.forward(size)
    turtle.end_fill()

def circle(x, y, size, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def triangle(x, y, size, color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.end_fill()

def skyline():
    floorX = -300
    size = 110
    rect(-860, floorX, 600, size, "black")
    rect(-750, floorX, 500, size, "black")
    rect(-640, floorX, 200, size, "black")
    rect(-530, floorX, 450, size, "black")
    rect(-420, floorX, 300, size, "black")
    rect(-310, floorX, 600, size, "black")
    rect(-200, floorX, 450, size, "black")
    rect(-90, floorX, 520, size, "black")
    rect(20, floorX, 220, size, "black")
    rect(130, floorX, 580, size, "black")
    rect(240, floorX, 670, size, "black")
    rect(350, floorX, 450, size, "black")
    rect(460, floorX, 600, size, "black")
    rect(570, floorX, 650, size, "black")
    rect(680, floorX, 550, size, "black")
    rect(790, floorX, 450, size, "black")

def background():
    size = 100
    rect(-860, 450, size, 1750, "#4e55a6")
    rect(-860, 350, size, 1750, "#ac1e8e")
    rect(-860, 250, size, 1750, "#d90e84")
    rect(-860, 150, size, 1750, "#ee0d69")
    rect(-860, 50, size, 1750, "#f04d22")
    rect(-860, -50, size, 1750, "#f8901f")
    rect(-860, -150, size, 1750, "#fff816")

    rect(-860, -550, 300, 1750, "#333333")

def decorations():
    star(-800, 360, 20, "yellow")
    star(-715, 340, 10, "yellow")
    star(-700, 320, 20, "yellow")
    star(-600, 360, 20, "yellow")
    star(-615, 320, 10, "yellow")
    star(-500, 300, 20, "yellow")
    star(-525, 320, 20, "yellow")
    star(-400, 330, 20, "yellow")
    star(-300, 320, 20, "yellow")
    star(-240, 360, 10, "yellow")
    star(-200, 350, 20, "yellow")
    star(-125, 335, 10, "yellow")
    star(-100, 360, 20, "yellow")
    star(0, 380, 20, "yellow")
    star(25, 340, 20, "yellow")
    star(100, 310, 20, "yellow")
    star(200, 330, 20, "yellow")
    star(270, 340, 20, "yellow")
    star(300, 315, 10, "yellow")
    star(400, 320, 30, "yellow")
    star(420, 310, 10, "yellow")
    star(500, 340, 20, "yellow")
    star(580, 315, 10, "yellow")
    star(620, 370, 40, "yellow")
    star(700, 315, 20, "yellow")
    star(760, 325, 20, "yellow")
    star(800, 300, 10, "yellow")

def clouds():
    circle(-620, 290, 40, "#ffad00")
    circle(-560, 310, 45, "#ffad00")
    circle(-520, 290, 45, "#ffad00")
    circle(-540, 260, 30, "#ffad00")
    circle(-585, 260, 30, "#ffad00")

    circle(-620, 300, 40, "#800080")
    circle(-560, 320, 45, "#800080")
    circle(-520, 300, 45, "#800080")
    circle(-540, 270, 30, "#800080")
    circle(-585, 270, 30, "#800080")

    circle(0, 245, 80, "#ffad00")
    circle(120, 265, 90, "#ffad00")
    circle(200, 245, 95, "#ffad00")
    circle(160, 215, 60, "#ffad00")
    circle(70, 215, 60, "#ffad00")

    circle(0, 260, 80, "#800080")
    circle(120, 280, 90, "#800080")
    circle(200, 260, 95, "#800080")
    circle(160, 230, 60, "#800080")
    circle(70, 230, 60, "#800080")

def main():
    turtle.bgcolor("blue")
    background()
    decorations()
    clouds()
    skyline()
    #triangle(0, 0, 100, "yellow")

    input("Press enter to continue...")

main()