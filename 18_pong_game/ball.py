from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 0)
        self.pensize(20)
        self.color("white")
        self.shape("circle")
        self.dir = (random.randint(-5, 5)/50, random.randint(-5, 5)/50)

    def move(self):
        self.goto(self.xcor() + self.dir[0], self.ycor() + self.dir[1])

    def bounce_y(self):
        self.dir = (self.dir[0], self.dir[1] * -1)

    def bounce_x(self):
        self.dir = (self.dir[0] * -1, self.dir[1])

    def reset_ball(self):
        self.setpos(0, 0)
        self.dir = (random.randint(-5, 5)/50, random.randint(-5, 5)/50)
