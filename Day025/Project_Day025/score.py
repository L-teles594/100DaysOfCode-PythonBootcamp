from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def increase(self):
        self.score += 1

    def is_over(self):
        return self.score == 50
