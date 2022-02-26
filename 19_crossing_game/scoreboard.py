from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-290, 270)
        self.level = 1

    def display_level(self):
        self.clear()
        self.write(f'Level: {self.level}', move=False, align='left', font=('Arial', 15, 'normal'))

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.setpos(0, 0)
        self.write(f'GAME OVER', move=False, align='center', font=('Arial', 30, 'normal'))

