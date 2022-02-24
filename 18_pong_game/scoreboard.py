from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.color('white')
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.setpos(0, 225)
        self.write('Score', move=False, align='center', font=('Arial', 15, 'normal'))
        self.setpos(0, 190)
        self.write(f'{self.player1_score}:{self.player2_score}', move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def player1_win(self):
        self.player1_score += 1
        self.display_score()

    def player2_win(self):
        self.player2_score += 1
        self.display_score()
