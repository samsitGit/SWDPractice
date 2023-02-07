import turtle

def rect(x, y, height, base, pencolor, fillcolor):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
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

def triangle(x, y, size, pencolor, fillcolor):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.end_fill()

def circle(x, y, size, pencolor, fillcolor):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(4)
    turtle.color(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def skyline():
    floorX = -300
    rect(-860, floorX, 600, 100, "black", "black")
    rect(-760, floorX, 500, 100, "black", "black")
    rect(-660, floorX, 200, 100, "black", "black")
    rect(-560, floorX, 650, 100, "black", "black")
    rect(-460, floorX, 300, 100, "black", "black")
    rect(-360, floorX, 600, 100, "black", "black")
    rect(-260, floorX, 450, 100, "black", "black")
    rect(-160, floorX, 550, 100, "black", "black")
    rect(-60, floorX, 400, 100, "black", "black")
    rect(40, floorX, 700, 100, "black", "black")
    rect(140, floorX, 550, 100, "black", "black")
    rect(240, floorX, 450, 100, "black", "black")
    rect(340, floorX, 600, 100, "black", "black")
    rect(440, floorX, 650, 100, "black", "black")
    rect(540, floorX, 550, 100, "black", "black")
    rect(640, floorX, 450, 100, "black", "black")
    rect(740, floorX, 250, 100, "black", "black")
    rect(840, floorX, 400, 100, "black", "black")

def main():
    turtle.bgcolor("blue")

    skyline()

    rect(-860, -550, 300, 1750, "gray", "gray")

    input("Press enter to continue...")

main()