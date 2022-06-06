from turtle import Screen
from player import Player
from scoreboard import Score
from cars import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
cars = Car()


screen.listen()
screen.onkey(fun=player.go_up, key='Up')

game_is_on = True
while game_is_on:
    screen.update()
    score.update_scoreboard()
    cars.get_new_car()
    cars.go_forward()

    # Is game over
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.is_game_over()

    # Pointing score
    if player.ycor() >= 280:
        score.increase_score()
        player.reset_turtle()
        cars.level_up()




screen.exitonclick()
