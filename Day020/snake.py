from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.unit = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.unit.forward(MOVE_DISTANCE)

    def up(self):
        if self.unit.heading() != DOWN:
            self.unit.setheading(UP)

    def down(self):
        if self.unit.heading() != UP:
            self.unit.setheading(DOWN)

    def right(self):
        if self.unit.heading() != LEFT:
            self.unit.setheading(RIGHT)

    def left(self):
        if self.unit.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
