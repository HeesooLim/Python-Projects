from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_pos, screen):
        super().__init__()
        self.x = x_pos
        self.screen = screen
        self.penup()
        self.setpos(x_pos, 0)
        self.pensize(12)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.distance(self.xcor(), 200) != 0:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.distance(self.xcor(), -200) != 0:
            self.goto(self.xcor(), self.ycor() - 20)
