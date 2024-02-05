import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Yakala şu turtleyi")
FONT = ('Arial', 15, 'bold')
score = 0
game_over = False

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

turtle_list = []

score_turtle = turtle.Turtle()

countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.setpos(0, 300)
    score_turtle.write(arg="Score= 0", move=False, align="center", font=FONT)


grid_size = 12


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score= {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5, 1.5)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


def turtle_position():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtle_random():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_random, 1000)


def countdown(time):
    global game_over
    countdown_turtle.color("dark blue")
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setpos(0, 280)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time Left= {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 750)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)


def game_start():
    turtle.tracer(0)
    setup_score_turtle()
    turtle_position()
    hide_turtles()
    show_turtle_random()
    countdown(20)
    turtle.tracer(1)


game_start()

turtle.mainloop()
