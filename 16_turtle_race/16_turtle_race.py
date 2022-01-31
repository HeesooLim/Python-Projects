#----------------------------------------------------------------------------
# File name   : 16_turtle_race.py
# Created By  : Heesoo Lim
# Created Date: 30/01/2022
# ---------------------------------------------------------------------------

import random
from turtle import Turtle, Screen, textinput

turtle_arena = Turtle()

colors = ["lightgreen", "gold", "gray", "orange", "darkgreen", "yellow"]


def draw_arena():
    turtle_arena.hideturtle()
    turtle_arena.speed("fastest")
    turtle_arena.penup()
    turtle_arena.setposition(-185, 130)
    turtle_arena.pendown()
    turtle_arena.forward(395)
    turtle_arena.right(90)
    turtle_arena.forward(215)
    turtle_arena.right(90)
    turtle_arena.forward(395)
    turtle_arena.right(90)
    turtle_arena.forward(215)


def create_turtles():
    turtles = []
    for i in range(6):
        new_turtle = Turtle()
        new_turtle.pencolor(colors[i])
        turtles.append(new_turtle)
    return turtles


def choose_shape(turtle_list):
    for t in turtle_list:
        t.shape("turtle")


def set_position(turtle_list):
    count = 0
    for t in turtle_list:
        t.penup()
        t.setposition(-170, 100 - (30 * count))
        count += 1


def move_forward(turtle_list):
    for t in turtle_list:
        t.forward(random.randint(1, 5))


def is_game_over(turtle_list):
    for t in turtle_list:
        x_pos = t.pos()[0]
        if x_pos > 170:
            return True
        return False


def find_winner(turtle_list):
    x_pos_list = [t.pos()[0] for t in turtle_list]
    return x_pos_list.index(max(x_pos_list))


guess_number = int(textinput("Turtle race!", "Guess a winner (between 1-6)"))
draw_arena()
my_turtles = create_turtles()
choose_shape(my_turtles)
set_position(my_turtles)

while not is_game_over(my_turtles):
    move_forward(my_turtles)

winner_number = find_winner(my_turtles) + 1
if guess_number == winner_number:
    print("You're right!")
else:
    print("Oops")
print(f"The winner is turtle {winner_number}.")
screen = Screen()
screen.exitonclick()
