from turtle import Turtle, Screen

# Draw a dashed line Challenge
tim = Turtle()
tim.shape("turtle")
tim.color("gold1")

for _ in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

my_screen = Screen()
my_screen.exitonclick()
