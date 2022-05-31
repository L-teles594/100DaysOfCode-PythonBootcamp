from turtle import Turtle, Screen

# Draw a square Challenge
timmy = Turtle()
timmy.shape('turtle')
timmy.color('gold1')

for _ in range(4):
    timmy.rt(90)
    timmy.fd(100)

my_screen = Screen()
my_screen.exitonclick()