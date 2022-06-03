from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('Arial', 24, 'normal'))

    def update_score_board(self):
        self.clear()
        self.write(f"score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score_board()
