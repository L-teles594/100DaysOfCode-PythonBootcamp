from snake import Snake
from turtle import Screen
from time import sleep
from Day021.food import Food
from Day021.scoreboard import Score

# The screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title(f'My Snake Game')

# the Snake and Food setup

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.left, key='a')


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect colision with food
    if snake.unit.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect colision with wall
    if snake.unit.xcor() > 280 or snake.unit.xcor() < -280 or snake.unit.ycor() > 290 or snake.unit.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect colision with tail

    for segment in snake.segments[1:]:
        if snake.unit.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()











