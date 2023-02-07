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

def skyline():
    floorX = -300
    size = 110
    rect(-860, floorX, 600, size, "black")
    rect(-750, floorX, 500, size, "black")
    rect(-640, floorX, 200, size, "black")
    rect(-530, floorX, 650, size, "black")
    rect(-420, floorX, 300, size, "black")
    rect(-310, floorX, 600, size, "black")
    rect(-200, floorX, 450, size, "black")
    rect(-90, floorX, 550, size, "black")
    rect(20, floorX, 200, size, "black")
    rect(130, floorX, 600, size, "black")
    rect(240, floorX, 650, size, "black")
    rect(350, floorX, 450, size, "black")
    rect(460, floorX, 600, size, "black")
    rect(570, floorX, 650, size, "black")
    rect(680, floorX, 550, size, "black")
    rect(790, floorX, 450, size, "black")

def background():
    size = 100
    rect(-860, 450, size, 1750, "blue")
    rect(-860, 350, size, 1750, "purple")
    rect(-860, 250, size, 1750, "magenta")
    rect(-860, 150, size, 1750, "violet")
    rect(-860, 50, size, 1750, "orange")
    rect(-860, -50, size, 1750, "gold")
    rect(-860, -150, size, 1750, "yellow")

    star(-800, 360, 20, "yellow")
    star(-750, 340, 20, "yellow")
    star(-600, 360, 20, "yellow")
    star(-500, 320, 20, "yellow")

    rect(-860, -550, 300, 1750, "gray")

def main():
    
    background()
    skyline()

    input("Press enter to continue...")

main()