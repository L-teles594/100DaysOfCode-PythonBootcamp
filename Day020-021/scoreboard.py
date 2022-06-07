from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.new_highscore()
        self.score = 0
        self.update_score_board()

    def new_highscore(self):
        with open('data.txt', mode='w') as data:
            data.write(str(self.highscore))
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align="center", font=('Arial', 24, 'normal'))

    def update_score_board(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.highscore}", align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score_board()
