import turtle

def draw_circle(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_centered_circle(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.forward(radius) #go radius away and draw circle from there
    turtle.left(90)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.left(90)
    turtle.up()
    turtle.forward(radius)
    turtle.left(180)
    
def draw_smiley():
    draw_centered_circle(0, 0, 100, "yellow")
    draw_centered_circle(0, 0, 20, "pink")

def main():
    #draw_circle(0, 0, 100, "white")
    #draw_circle(-200, -20, 30, "yellow")
    #draw_circle(200, -20, 50, "blue")
    #draw_centered_circle(0, 0, 50, "blue")
    draw_smiley()
    input("Press enter to continue...")

main()