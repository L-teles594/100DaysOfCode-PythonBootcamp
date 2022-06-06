from turtle import Turtle
WIDTH = 5
HEIGHT = 1
INIT_POSITION = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, paddle_num):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.turtlesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.paddle = paddle_num
        self.get_new_position()

    def get_new_position(self):
        self.penup()
        self.goto(INIT_POSITION[self.paddle])

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)
