import turtle
import random

turtle.colormode(255)
screen = turtle.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

t = turtle.Turtle()
t.speed("fastest")
def size(s):
    for _ in range(360//s):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + s)

size(5)


screen.title("Spirograph")
screen.exitonclick()