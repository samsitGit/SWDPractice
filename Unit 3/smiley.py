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
    
def draw_smiley(x, y, face_size, eye_color):

    eye_x = x + face_size * .35
    eye_x2 = x - face_size * .35
    eye_y = y + face_size * .25
    eye_size = .25 * face_size
    mouth_x = x
    mouth_y = y - (face_size * .25)
    mouth_size = .6*face_size

    draw_centered_circle(x, y, face_size, "yellow")
    draw_centered_circle(x, y, .1*face_size, "pink")
    draw_eye(eye_x2, eye_y, eye_size, eye_color)
    draw_eye(eye_x, eye_y, eye_size, eye_color)
    draw_mouth(mouth_x, mouth_y, mouth_size, "black")

def tweak():
    turtle.speed(1)
    turtle.forward(100)
    turtle.left(90)
    turtle.tracer(False)
    turtle.circle(50)
    turtle.tracer(True)
    turtle.hideturtle()

def draw_eye(x, y, radius, iris_color):
    draw_centered_circle(x, y, radius, "white")
    draw_centered_circle(x, y, .5*radius, iris_color)
    draw_centered_circle(x, y, .25*radius, "black")

def draw_mouth(x, y, radius, fill_color):
    turtle.up()
    turtle.goto(x, y)
    turtle.forward(-(radius))
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(radius, 180)
    turtle.end_fill()
    turtle.right(90)
    turtle.up()
    turtle.forward(radius)

def main():

    #draw_circle(0, 0, 100, "white")
    #draw_circle(-200, -20, 30, "yellow")
    #draw_circle(200, -20, 50, "blue")
    #draw_centered_circle(0, 0, 50, "blue")
    #draw_smiley()
    #tweak()
    turtle.speed(0)
    draw_smiley(0, 0, 150, "blue")
    draw_smiley(-150, -150, 50, "blue")
    draw_smiley(200, 200, 200, "blue")
    draw_smiley(-200, 100, 80, "blue")
    draw_smiley(250, -200, 120, "blue")

    input("Press enter to continue...")

main()