import turtle
import random
import time

H = 500
W = 800

screen = turtle.Screen()
screen.setup(width = W, height = H)
screen.bgcolor("black")
screen.title("Pong")

rectangle = ((0, 0), (0,90), (10,90), (10,0))  
screen.register_shape("rectangle", rectangle)


border = turtle.Turtle()
border.pensize(1)
border.color("white")
border.penup()
border.goto(385,235)
border.pendown()
border.goto(385,-225)
border.goto(-385,-225)
border.goto(-385,235)
border.goto(390,235)
border.color("black")
    
s1 = 0
s2 = 0

score1 = turtle.Turtle()
score1.penup()
score1.color("white")
score1.hideturtle()
score1.goto(200, 140)
score1.write(f"{s1} \nPlayer 2", align="center", font=("Arial", 20, "normal"))

def update_score1():
    score1.clear()
    global s1
    s1 += 1
    score1.write(f"Score: {s1} \nPlayer 2", align="center", font=("Arial", 20, "normal"))

score2 = turtle.Turtle()
score2.penup()
score2.color("white")
score2.hideturtle()
score2.goto(-200, 140)
score2.write(f"{s2} \nPlayer 1", align="center", font=("Arial", 20, "normal"))

def update_score2():
    score2.clear()
    global s2
    s2 += 1
    score2.write(f"Score: {s2} \nPlayer 1", align="center", font=("Arial", 20, "normal"))


line = turtle.Turtle()
line.pensize(5)
line.color("white")
line.penup()
line.goto(0,235)
line.setheading(270)
for i in range(50):
    line.pendown()
    line.forward(5)
    line.penup()
    line.forward(10)
    if (line.ycor() < -225):
        break

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
    

p1 = turtle.Turtle()
p1.penup()
p1.shape("rectangle")
p1.color("white")
p1.goto(-390,0)
p1.setheading(90)
p1.speed(10)

p2 = turtle.Turtle()
p2.shape("rectangle")
p2.color("white")
p2.penup()
p2.goto(375,0)
p2.setheading(90)
p2.speed(10)


def up1():
    y = p1.ycor()
    if (y <= 140):
        p1.forward(10)

def down1():
    y = p1.ycor()
    if (y >= -220):
        p1.backward(10)

def up2():
    y = p2.ycor()
    if (y <= 140):
        p2.forward(10)

def down2():
    y = p2.ycor()
    if (y >= -220):
        p2.backward(10)
    
def game_over():
    screen.bye()
    print("Game Ended")

screen.listen()
screen.onkeypress(key = "w", fun = up1)
screen.onkeypress(key = "Up", fun = up2)
screen.onkeypress(key = "s", fun = down1)
screen.onkeypress(key = "Down", fun = down2)
screen.onkeypress(key = "Escape", fun = game_over)

def speed_change():
    speeds = [10,15,20]
    return random.choice(speeds)

def contact1():
    if (ball.xcor() < -365 and ball.xcor() > -375) and (ball.ycor() < p1.ycor() + 90 and ball.ycor() > p1.ycor()):
        return 1
    else:
        return 0
    
def contact2():
    if (ball.xcor() > 365 and ball.xcor() < 375) and (ball.ycor() < p2.ycor() + 90 and ball.ycor() > p2.ycor()):
        return 1
    else:
        return 0

def ballmovement():
    game = True
    ball.setheading(random.choice([random.randint(30, 60), random.randint(120, 150)]))
    while game:
        ball.forward(5)
        x = ball.xcor()
        y = ball.ycor()
        d1 = contact1()
        d2 = contact2()
        if (x > 375):
            print("Player 2 gets a point")
            update_score2()
            ball.goto(0,0)
            time.sleep(2)
            ball.setheading(random.choice([random.randint(30, 60), random.randint(120, 150)]))
            continue
        elif ( x < -390):
            print("Player 1 gets a point")
            update_score1()
            ball.goto(0,0)
            time.sleep(2)
            ball.setheading(random.choice([random.randint(30, 60), random.randint(120, 150)]))
            continue
        elif(y > 220 or y < -220):
            h = ball.heading()
            ball.setheading(360-h)
        elif (d1 == 1):
            ball.setheading(180 - ball.heading())
            ball.forward(speed_change())
        elif (d2 == 1):
            ball.setheading(180 - ball.heading())
            ball.forward(speed_change())
            
            
ballmovement()

screen.mainloop()

screen.exitonclick()