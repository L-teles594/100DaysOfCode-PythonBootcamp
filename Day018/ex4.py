import turtle as t
from random import choice, randint

# Drawing 8 different shapes in 8 different colors challenge


tim = t.Turtle()
tim.pensize(10)
direction = (0, 90, 180, 270)
tim.speed(10)
t.colormode(255)

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue


for _ in range(500):
    tim.pencolor(random_color())
    tim.setheading(choice(direction))
    tim.forward(20)


my_screen = t.Screen()
my_screen.exitonclick()
