from turtle import Turtle
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.level = 1
        self.penup()
        self.goto(-290, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_score(self):
        self.level += 1

    def is_game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)