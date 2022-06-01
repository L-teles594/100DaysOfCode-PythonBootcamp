import turtle as t


def go_forward():
    tim.forward(10)


def go_backward():
    tim.back(10)


def counter_clockwise():
    new_angle = tim.heading() + 5
    tim.setheading(new_angle)


def clockwise():
    new_angle = tim.heading() - 5
    tim.setheading(new_angle)


def clear_screen():
    screen.reset()


tim = t.Turtle()

screen = t.Screen()
screen.listen()

screen.onkey(key='w', fun=go_forward)
screen.onkey(key='s', fun=go_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
