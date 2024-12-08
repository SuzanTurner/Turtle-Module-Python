import turtle
import random
import time

chances = 7

screen = turtle.Screen()
screen.setup(width = 500, height = 450)
screen.bgcolor("#ADD8E6")

screen.title("Turtle Hangman")

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(-35,150)
title.write("Hangman", font = ("Ariel", 15, "bold"))

def middle_finger():
    screen.tracer(0)
    mf = turtle.Turtle()
    def draw_square(size):
        for _ in range(4):
            mf.forward(size)
            mf.left(90)

    mf.penup()
    mf.goto(125, 125)
    mf.pendown()

    block_size = 10

    coordinates = [
        (0, 0), (block_size, 0), (2*block_size, 0),
        (-block_size, block_size), (0, block_size), (block_size, block_size), (2*block_size, block_size), (3*block_size, block_size),
        (-2*block_size, 2*block_size), (-block_size, 2*block_size), (0, 2*block_size), (block_size, 2*block_size), (2*block_size, 2*block_size), (3*block_size, 2*block_size), (4*block_size, 2*block_size),
        (-2*block_size, 3*block_size), (-block_size, 3*block_size), (0, 3*block_size), (block_size, 3*block_size), (2*block_size, 3*block_size), (3*block_size, 3*block_size), (4*block_size, 3*block_size),
        (0, 4*block_size), (block_size, 4*block_size), (2*block_size, 4*block_size),(3*block_size, 4*block_size),(-1*block_size, 4*block_size),
        (block_size, 5*block_size), (block_size, 6*block_size), (block_size, 7*block_size)
    ]

    for coord in coordinates:
        mf.penup()
        mf.goto(125 + coord[0], 125 + coord[1])  
        mf.pendown()
        draw_square(block_size)

    mf.hideturtle()

    screen.update()

def end_program():
    ch.clear()
    ch.write("Game Over", font=("Comic Sans", 15, "bold"))
    time.sleep(3)
    screen.bye()

words = ["PATLE", "LEMON", "CHEST", "LEGS", "ARMS", "POLICE", "GYM", "DUMBO","KEYBOARD"]
w = random.choice(words)
l = len(w)

d = True
i = 10
while l>0:
    dash = turtle.Turtle()
    dash.penup()
    dash.hideturtle()
    dash.goto(-100+i, -150)
    dash.write("___")
    i = i + 30
    l = l - 1

hm = turtle.Turtle()
hm.hideturtle()
hm.penup()
hm.goto(-100, -100)
hm.pendown()
hm.goto(-100, 100)
hm.goto(60, 100)
hm.goto(60, 80)

ch = turtle.Turtle()
ch.hideturtle()
ch.penup()
ch.goto(-50,-200)
ch.write(f"Chances:{chances} ", font = ("Comic Sans", 13, "bold"))

def drawman():
    if chances ==  6:
        hm.penup()
        hm.goto(60, 40)
        hm.pendown()
        hm.circle(20)
    if chances == 5:
        hm.penup()
        hm.goto(60,40)
        hm.pendown()
        hm.goto(60,-40)
    if chances == 4:
        hm.goto(80,-60)
    if chances == 3:
        hm.penup()
        hm.goto(60,-40)
        hm.pendown()
        hm.goto(40,-60)
    if chances == 2:
        hm.penup()
        hm.goto(60, 20)  
        hm.pendown()
        hm.goto(80, 0)  
    if chances == 1:
        hm.penup()
        hm.goto(60, 20)  
        hm.pendown()
        hm.goto(40, 0) 

letter = screen.textinput(title = "Letter", prompt = "Enter a letter")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def game_over():
    title.clear()
    title.write("Game Over", font = ("Ariel", 15, "bold"))

def draw_letter(letter,index):
        let = turtle.Turtle()
        let.hideturtle()
        let.penup()
        if index == 0:
            let.goto(-90, -150)
        elif index == 1:
            let.goto(-60, -150)
        elif index == 2:
            let.goto(-30, -150)
        elif index == 3:
            let.goto(0, -150)
        elif index == 4:
            let.goto(30, -150)
        elif index == 5:
            let.goto(60, -150)
        elif index == 6:
            let.goto(90, -150)
        elif index == 7:
            let.goto(120, -150)
        
        let.write(f"{letter.upper()}", font = ("Sans Serif", 15, "bold"))

while chances > 0:
    if letter.upper() in w and letter.upper() in letters:
        index = w.find(letter.upper())    
        draw_letter(letter,index)
        letter = screen.textinput(title = "Letter", prompt = "Enter a letter")
    else:
        chances = chances - 1
        ch.clear()
        ch.write(f"Chances:{chances} ", font = ("Comic Sans", 13, "bold"))
        letter = screen.textinput(title = "Letter", prompt = "Enter a letter")
        drawman()
if chances == 0:
    middle_finger()
    game_over()
    end_program()

screen.update()


screen.exitonclick()