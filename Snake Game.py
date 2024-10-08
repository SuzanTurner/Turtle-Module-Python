import turtle
import random
import time

turtle.colormode(255)

s = turtle.Turtle()
s.color(0,150,255)
s.speed(0)


screen = turtle.Screen()
screen.setup(width = 500, height = 500)
screen.bgcolor(0,255,150)
screen.tracer(0)
screen.title("Snake Game")

score = 0

score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 210)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

s.penup()

def border():
    b = turtle.Turtle()
    b.color("black")
    b.penup()
    b.goto(220, 220)
    b.pendown()
    b.goto(220,-220)
    b.goto(-220,-220)
    b.goto(-220,220)
    b.goto(220, 220)
    b.penup()
    b.shape("blank")


border()

def right():
    s.setheading(0)
    s.forward(10)

def left():
    s.setheading(180)
    s.forward(10)

def top():
    s.setheading(90)
    s.forward(10)

def down():
    s.setheading(270)
    s.forward(10)

segs = [s]
positions = [(0,0), (20,0), (40,0), (60,0)]

seg = turtle.Turtle()
for pos in positions:
    #seg = turtle.Turtle()
    seg.penup()
    seg.shape("square")
    seg.color(0,150,255)
    seg.goto(pos)
    segs.append(seg)


screen.listen()
screen.onkeypress(key = "d", fun = right)
screen.onkeypress(key = "a", fun = left)
screen.onkeypress(key = "w", fun = top)
screen.onkeypress(key = "s", fun = down)

f = turtle.Turtle()
f.shape("circle")
f.color("red")
f.penup()
def food():
    x = random.randint(-210, 210)
    y = random.randint(-210,210)
    f.goto(x,y)
food()
    

game = True

while game:
    screen.update()
    time.sleep(0.1)

    for i in range(len(segs)-1, 0, -1):
        segs[i].goto(segs[i-1].pos())
    s.forward(20)

    if s.distance(f) < 15:
        food()
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color(0, 150, 255)
        new_segment.penup()
        segs.append(new_segment)
        score += 1
        update_score()

    if abs(s.xcor()) > 220 or abs(s.ycor()) > 220:
        game = False

    for segment in segs[1:]:
        if s.distance(segment) < 10:
            game = False

screen.exitonclick()