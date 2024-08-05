import turtle
import random

turtle.colormode(255)
r = 0
g = 0
b = 0
def randcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour


t = turtle.Turtle()
t.shape("arrow")
t.pensize(10)
directions = [0,90,180,270]
t.speed(10)
for _ in range (1000):
    colors = (r,g,b)
    t.color(randcolor())
    t.forward(20)
    d = random.choice(directions)
    t.right(d)

