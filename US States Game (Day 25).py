import turtle
import pandas
import time

data = pandas.read_csv(r"D:\Yadh Documents\100 Days of Code Python\50_states.csv")

screen = turtle.Screen()
screen.title("US States")

image = r"D:\Yadh Documents\100 Days of Code Python\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

clock = turtle.Turtle()
clock.penup()
clock.goto(260, 250)
clock.hideturtle()

s = 300  

def countdown():
    global s
    if s > 0:
        m = s // 60
        sec = s % 60
        clock.clear()
        clock.write(f"{m}:{sec:02d}", align="center", font=("Arial", 12, "normal"))
        s -= 1
        screen.ontimer(countdown, 1000)  
    else:
        clock.clear()
        clock.goto(0, 0)
        clock.write("Time's Up", align="center", font=("Arial", 20, "normal"))
        time.sleep(3)
        screen.bye()


countdown()

score = turtle.Turtle()
score.penup()
score.goto(-260, 250)
score.hideturtle()
s_val = 0

states = data.state.to_list()
x = data.x
y = data.y

xy = list(zip(x, y))
d = dict(zip(states, xy))

for i in range(50):
    ans = screen.textinput(title="Guess the State", prompt="What's the state's name?")
    
    if ans is None:
        break  
    answer = ans.title()
    if answer in states:
        t = turtle.Turtle()
        t.penup()
        t.color("black")
        t.hideturtle()
        a, b = d[answer]
        t.goto(a, b)
        t.write(f"{answer}", align="center", font=("Arial", 10, "normal"))
        score.clear()
        s_val += 1
        score.write(f"Score: {s_val}/50", align="center", font=("Arial", 12, "normal"))


turtle.mainloop()