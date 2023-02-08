import turtle

def draw_circle(x, y, radius, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()


def main():
    draw_circle(0, 0, 100, "white")
    draw_circle(-200, -20, 30, "yellow")
    draw_circle(200, -20, 50, "blue")
    input("Press enter to continue...")

main()