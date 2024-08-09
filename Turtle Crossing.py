import turtle
import random
import time

turtle.colormode(255)

screen = turtle.Screen()
screen.setup(600,400)
screen.title("Turtle Crossing")
brick = ((0,0), (0,40), (10,40), (10,0))
screen.register_shape("brick", brick)

t = turtle.Turtle()
t.penup()
t.color("magenta")
t.shape("turtle")
t.setheading(90)
t.goto(0,-165)

f = turtle.Turtle()
f.penup()
f.pensize(5)
f.color("black")
f.goto(-270, 180)
while (f.xcor() < 270):
    f.pendown()
    f.forward(5)
    f.penup()
    f.forward(10)
f.color("white")

def randcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

def speed():
    speeds = [1,2,3]
    s = random.choice(speeds)
    return s

def up():
    t.forward(5)
def down():
    t.backward(5)
def end():
    screen.bye()

screen.listen()
screen.onkeypress(key = "Up", fun = up)
screen.onkeypress(key = "Down", fun = down)
screen.onkeypress(key = "Escape", fun = end)

bricks = []

def move():
    for b in bricks[:]:
        b.backward(speed())
        if b.xcor() < -300:
            b.hideturtle()
            bricks.remove(b)

def brick():
    while (len(bricks) < 20):
        b = turtle.Turtle()
        b.penup()
        b.shape("brick")
        b.color("white")
        b.goto(240, (random.randint(-13,14) * 10)) or b.goto((random.randint(-240,240)), (random.randint(-13,14) * 10))
        b.color(randcolor())
        bricks.append(b)

def contact():
   for b in bricks:
        if abs(t.xcor() - b.xcor()) < 10 and abs(t.ycor() - b.ycor()) < 10:
            return 1
   return 0
    
turtle.tracer(0)

game = True
while game:
    game_over = turtle.Turtle()
    game_over.penup()
    game_over.color("black")
    game_over.goto(0,0)
    win = turtle.Turtle()
    win.penup()
    win.color("black")
    win.goto(0,0)
    brick()
    move()
    turtle.update()
    time.sleep(0.1)
    if (t.ycor() > 150):
        win.write("You Win!!", align = "center", font = ("Ariel", 20, "normal"))
    elif (contact() == 1):
        game_over.write("Game Over", align="center", font=("Arial", 20, "normal"))
        game = False

screen.exitonclick()