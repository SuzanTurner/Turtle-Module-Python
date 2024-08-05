import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)

t.pensize(5)

def gencolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

screen = turtle.Screen()
screen.setup(width=500, height=500)

t.penup()
t.speed("fastest")
X = -230
Y = 230
t.goto(X, Y)
t.pendown()
while True:
    t.color(gencolor())
    t.forward(1)
    t.penup()
    t.forward(15)
    t.pendown()
    x,y = t.pos()
    if (x > 230):
        t.penup()
        Y = Y - 15
        t.goto(X, Y)
        t.pendown()

    if (y < -230):
        break
    
screen.exitonclick()

