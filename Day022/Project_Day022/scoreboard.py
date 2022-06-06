from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f'{self.score_l}   {self.score_r}', align='center', font=('Courier', 30, 'bold'))

    def increase_score_r(self):
        self.score_r += 1

    def increase_score_l(self):
        self.score_l += 1
