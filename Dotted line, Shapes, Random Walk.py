import turtle
import random

screen = turtle.Screen()

r = turtle.Turtle()
r.shape("arrow")
r.color("blue")
for _ in range(10):
    r.forward(10)
    r.penup()
    r.forward(10)
    r.pendown()

t = turtle.Turtle()
t.shape("arrow")
t.color("cyan")
t.penup()
t.goto(-100, 100)
t.pendown()
n = 3
a = 0
for _ in range(10):
    for _ in range(n):
        a = 180 - (360/n)
        t.forward(100)
        t.right(180-a)
    n += 1

p = turtle.Turtle()
p.shape("square")
colors = [
    "red", "green", "blue", "yellow", "orange", "purple",
    "brown", "black", "gray", "pink", "cyan", "magenta",
    "lime", "maroon", "navy", "olive", "teal", "violet", "gold",
    "silver", "beige", "coral", "indigo", "khaki", "lavender", "salmon",
    "sienna", "turquoise", "wheat"
]
turn = [90, 180, 270 ]
for _ in range(1000):
    p.forward(15)
    c = random.choice(colors)
    t = random.choice(turn)
    p.color(c)
    p.right(t)
    p.speed(10)



screen.exitonclick()