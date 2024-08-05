import turtle

t = turtle.Turtle()
t.shape("arrow")
screen = turtle.Screen()


def movefd():
    t.forward(10)

def movebk():
    t.backward(10)

def turnright():
    h = t.heading - 10
    t.right(h)
    

def turnleft():
    h = t.heading() + 10
    t.left(h)

def clear():
    t.clear()
    t.penup()
    t.goto(0,0) #or can use t.home()
    t.pendown()


screen.listen()
screen.onkey(key = "w", fun = movefd )
screen.onkey(key = "s", fun = movebk)
screen.onkey(key = "d", fun = turnright)
screen.onkey(key = "a", fun = turnleft)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()