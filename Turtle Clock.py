import turtle
import datetime

screen = turtle.Screen()
screen.setup(width = 450, height=400)
screen.title("Turtle Clock")
screen.bgcolor("#E0FBFC")

label = turtle.Turtle()
label.penup()
label.goto(-90,140)
label.write("Turtle Clock", font = ("Courier", 20, "bold"))
label.hideturtle()

def border():
    screen.tracer(0)
    b = turtle.Turtle()
    b.color("white")
    b.pensize(2)
    b.penup()
    b.goto(-100, 140)
    b.pendown()
    b.goto(110,140)
    b.goto(110,170)
    b.goto(-100,170)
    b.goto(-100, 140)
    b.hideturtle()

border()

minute_hand = ((-2,0), (2,0),(0,70))
screen.register_shape("minute_hand", minute_hand)

hour_hand = ((-3,0), (3,0), (0,60))
screen.register_shape("hour_hand", hour_hand)

second_hand = ((-1,0), (1,0), (0,75))
screen.register_shape("second_hand", second_hand)

clock = turtle.Turtle()
clock.shape("circle")
clock.pensize(4)
def draw_clock():
    screen.tracer(0)
    clock.penup()
    clock.goto(0,-100)
    clock.pendown()
    clock.circle(100)
    clock.hideturtle()
    number = turtle.Turtle()
    number.penup()
    number.goto(80,-8)
    number.write(3, font = ("Geogia", 12, "bold"))
    number.goto(0,-90)
    number.write(6, font = ("Geogia", 12, "bold"))
    number.goto(-85,-10)
    number.write(9, font = ("Geogia", 12, "bold"))
    number.goto(-5,75)
    number.write(12, font = ("Geogia", 12, "bold"))
    number.hideturtle()
    
draw_clock()

mh = turtle.Turtle()
mh.penup()
mh.color("#3D5A80")
mh.shape("minute_hand")
mh.setheading(90)

hh = turtle.Turtle()
hh.penup()
hh.color("#293241")
hh.shape("hour_hand")
hh.setheading(90)

sh = turtle.Turtle()
sh.penup()
sh.color("#261C15")
sh.shape("second_hand")
sh.setheading(90)


def change_second(s):
    sh.setheading(-s-270)


def change_minute(m):
    mh.setheading(-m-270)


def change_hour(h):
    hh.setheading(-h-270)

clock = turtle.Turtle()
clock.penup()
clock.goto(-40,-150)
clock.hideturtle()

def clock_time(hour, minute, second):
    clock.clear()
    clock.write(f"{hour:02d}:{minute:02d}:{second:02d}", font = ("Courier", 15, "bold"))

def change_time():
    screen.tracer(0)
    now = datetime.datetime.now()
    minute = now.minute
    hour = now.hour
    second = now.second
    s = second * 6
    m = minute * 6
    h = int((hour % 12) * 30 + minute * 0.5)
    change_second(s)
    change_minute(m)
    change_hour(h)
    clock_time(hour, minute,second)
    screen.update()
    screen.ontimer(change_time, 1000)

    
change_time()

screen.exitonclick()