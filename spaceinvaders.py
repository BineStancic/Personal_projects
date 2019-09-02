import turtle

wn = turtle.Screen()
wn.title("Space Invaders")

wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#draw ship
ship = turtle.Turtle()
ship.speed(0)
ship.shape("classic")
ship.color("white")
ship.tilt(90)
ship.shapesize(2,2)
ship.penup()
ship.goto(0, -250)

#draw shields
shield = turtle.Turtle()
shield.shape("square")
shield.color("white")
shield.penup()
shield.shapesize(stretch_wid = 1, stretch_len = 5)
shield.goto(-300, -200)

shield = turtle.Turtle()
shield.shape("square")
shield.color("white")
shield.penup()
shield.shapesize(stretch_wid = 1, stretch_len = 5)
shield.goto(300, -200)

shield = turtle.Turtle()
shield.shape("square")
shield.color("white")
shield.penup()
shield.shapesize(stretch_wid = 1, stretch_len = 5)
shield.goto(-100, -200)

shield = turtle.Turtle()
shield.shape("square")
shield.color("white")
shield.penup()
shield.shapesize(stretch_wid = 1, stretch_len = 5)
shield.goto(100, -200)


#import and register alien gif
gif = r"C:\Users\bstancic\Downloads\alien.gif"
turtle.register_shape(gif)
#draw alien
alien = turtle.Turtle()
alien.shape(gif)
alien.shapesize(2,2)

def move_left():
    x = ship.xcor()
    x -= 10
    ship.setx(x)

def move_right():
    x = ship.xcor()
    x += 10
    ship.setx(x)


wn.listen()
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")

while True:
    wn.update()
