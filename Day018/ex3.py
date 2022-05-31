from turtle import Turtle, Screen

# Drawing 8 different shapes in 8 different colors challenge

tim = Turtle()
tim.shape('turtle')
colors = ('gray0', 'gold1', 'DodgerBlue4', 'green', 'navy', 'orange4', 'yellow2', 'tomato4')
lines = 3

for i in range(8):
    tim.color(colors[i])
    angle = 360 / lines
    for j in range(lines):
        tim.forward(100)
        tim.rt(angle)
    lines += 1

my_screen = Screen()
my_screen.exitonclick()