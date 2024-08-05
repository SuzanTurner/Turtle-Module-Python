import turtle
import random

race = False

finish = turtle.Turtle()
screen = turtle.Screen()
screen.title("Turtle Race")
bet = screen.textinput(title =  "Make your choice", prompt = "Which color do you think would win?")



H = 500
W = 500

screen.setup(width = W, height = H)

finish.penup()
finish.shape("square")
finish.goto(220, 230)
finish.pendown()

def dotted1():
    finish.right(90)
    for _ in range (500):
        finish.pendown()
        finish.pensize(5)
        finish.color("black")
        finish.forward(2)
        finish.penup()
        finish.forward(10)
        x,y = finish.pos()
        if (y < - 230):
            break
def dotted2():
    for _ in range (500):
        finish.pendown()
        finish.pensize(5)
        finish.color("black")
        finish.forward(2)
        finish.penup()
        finish.forward(10)
        x,y = finish.pos()
        if (y < - 230):
            break
    
dotted1()
finish.goto(225,223)
dotted2()
finish.color("white")

Y = [60,30,0,-30,-60, -90]
turtles = []

colors = ["brown", "blue", "indigo", "green", "orange", "magenta"]
for i in range(0,6):
    t = turtle.Turtle() #has to be initialised again and again, therefore inside the loop
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x = -230, y = Y[i])
    turtles.append(t)

if bet:
    race = True

while race:
    for turtle in turtles:
        d = random.randint(0,10)
        turtle.forward(d)
        X,Y = turtle.pos()
        if (X>220):
            race = False
            if (bet.lower() == turtle.pencolor()):
                print("You Won!!")
            else:
                print(f"You lost, {turtle.pencolor()} has won")





screen.exitonclick()


