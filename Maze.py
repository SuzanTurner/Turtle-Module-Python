import turtle
import random
import time

screen = turtle.Screen()
screen.setup(width = 600, height = 500)
rect = ((0, 0), (0,60), (10,60), (10,0))
screen.register_shape("rect", rect)
screen.title("Maze")


msg = turtle.Turtle()
msg.penup()
msg.color("black")

border = turtle.Turtle()
border.pensize(10)
border.color("black")
border.penup()
border.goto(-290, -235)
border.pendown()
border.goto(-290,240)
border.goto(285,240)
border.penup()
border.goto(285, -235)
border.pendown()
border.goto(-290,-235)
border.hideturtle()

turtle.colormode(255)

def randcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
    

t = turtle.Turtle()
t.penup()
t.color(randcolor())
t.shape("circle")
t.goto(-270,-215)

def mouse_cursor(x,y):
    t.goto(x,y)

h = turtle.Turtle()
hurdles =[]

xcors = [i for i in range(-230,260,60)]
ycors = [j for j in range(-220, 210, 60)]

def hurdle():
    screen.tracer(0)
    for i in range(100):
        h = turtle.Turtle()
        h.penup()
        h.color("black")
        h.shape("rect")
        x = random.choice(xcors)
        y = random.choice(ycors)
        heading = [0,90]
        h.setheading(random.choice(heading))
        h.goto(x,y)
        hurdles.append(h)
        screen.update()

def follow_mouse():
    x = screen.cv.winfo_pointerx() - screen.cv.winfo_rootx() - screen.window_width() // 2
    y = screen.window_height() // 2 - (screen.cv.winfo_pointery() - screen.cv.winfo_rooty())
    t.goto(x, y)
    screen.ontimer(follow_mouse, 50)
    if t.xcor() > 290:
        msg.write("You Won!!", align = "center", font = ("Ariel", 20, "bold"))
        screen.update()
        time.sleep(5)
        screen.bye()
    screen.update()

def follow(x,y):
    t.goto(x,y)

def contact():
    for i in hurdles:
        t_left = t.xcor() - 5
        t_right = t.xcor() + 5
        t_top = t.ycor() + 5
        t_bottom = t.ycor() - 5
        
        if i.heading() == 90:
            h_left = i.xcor() - 5
            h_right = i.xcor() + 5
            h_top = i.ycor() + 60
            h_bottom = i.ycor() - 5
            if t_right > h_left and t_left < h_right and t_top > h_bottom and t_bottom < h_top:
                msg.clear()
                msg.goto(0, 0)
                msg.write("Game Over", align="center", font=("Arial", 20, "normal"))
                screen.update()
                time.sleep(3)
                screen.bye()
                return True  
        else:
            h_left = i.xcor() - 5
            h_right = i.xcor() + 60
            h_top = i.ycor() + 5
            h_bottom = i.ycor() - 5
            if t_right > h_left and t_left < h_right and t_top > h_bottom and t_bottom < h_top:
                msg.clear()
                msg.goto(0, 0)
                msg.write("Game Over", align="center", font=("Arial", 20, "normal")) 
                screen.update()
                time.sleep(3)
                screen.bye()
                return True
                 
    return False 

def check_for_collision():
    if not contact():
        screen.ontimer(check_for_collision, 10)

follow_mouse()
hurdle()
check_for_collision()
screen.update()
screen.mainloop()