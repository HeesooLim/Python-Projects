#----------------------------------------------------------------------------
# File name   : 15_art_dots.py
# Created By  : Heesoo Lim
# Created Date: 30/01/2022
# ---------------------------------------------------------------------------

from turtle import Turtle, Screen
import random
import colorgram

my_turtle = Turtle()
screen = Screen()

# extract colors from the picture
colors = colorgram.extract('img.jpg', 10)

my_turtle.pensize(7)
my_turtle.hideturtle()
my_turtle.speed("fastest")
screen.colormode(255)


def draw_dot_and_move():
    my_turtle.pendown()
    my_turtle.dot()
    my_turtle.penup()
    my_turtle.forward(30)


for a in range(1, 60):
    if a % 12 == 0:
        # get the current Y position of the turtle
        positionY = my_turtle.pos()[1]
        # reset the position of the turtle
        my_turtle.setpos(0, positionY + 30)
    # change the color of the pen
    my_turtle.pencolor(random.choice(colors).rgb)
    draw_dot_and_move()

screen.exitonclick()
