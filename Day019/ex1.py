import turtle as t


def move_forward():
    tim.forward(10)


tim = t.Turtle()


my_screen = t.Screen()
my_screen.listen()
my_screen.onkey(key='space', fun=move_forward)
my_screen.exitonclick()
