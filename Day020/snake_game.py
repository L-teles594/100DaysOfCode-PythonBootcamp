from snake import Snake
from turtle import Screen
from time import sleep


# Moving functions
def go_up():
    for square in snake:
        square.setheading(directions[1])


def go_down():
    for square in snake:
        square.setheading(directions[3])


def go_right():
    for square in snake:
        square.setheading(directions[0])


def go_left():
    for square in snake:
        square.setheading(directions[2])


# The screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title(f'My Snake Game')
# Snake setup

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.left, key='a')

while True:
    screen.update()
    sleep(0.1)
    snake.move()

screen.exitonclick()








