import turtle as t


def get_color():
    from random import randint
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue


tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.pencolor(get_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(1)

my_screen = t.Screen()
my_screen.exitonclick()
