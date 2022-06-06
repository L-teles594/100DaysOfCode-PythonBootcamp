from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


re_paddle = Paddle(paddle_num=0)
lt_paddle = Paddle(paddle_num=1)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=re_paddle.go_up, key='Up')
screen.onkey(fun=re_paddle.go_down, key='Down')
screen.onkey(fun=lt_paddle.go_up, key='w')
screen.onkey(fun=lt_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    ball.wall_colision()

    right_contact = ball.distance(re_paddle) < 50 and ball.xcor() > 340
    left_contact = ball.distance(lt_paddle) < 50 and ball.xcor() < -340

    if right_contact or left_contact :
        ball.ball_colision()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.increase_score_l()

    if ball.xcor() < - 380:
        ball.ball_reset()
        score.increase_score_r()

    score.update_score_board()

screen.exitonclick()