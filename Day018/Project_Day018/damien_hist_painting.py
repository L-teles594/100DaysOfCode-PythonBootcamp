import turtle as t
from random import choice
# from colorgram import extract
#
# colors = extract('image.jpg', 30)
# rgb_colors = list()
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))


def draw_line():
    tim.pencolor(choice(rgb_colors))
    tim.pendown()
    tim.forward(1)
    tim.penup()
    tim.forward(50)


rgb_colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101),
              (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7),
              (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77),
              (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

tim = t.Turtle()
t.colormode(255)
tim.pensize(20)
y = -200
tim.speed('fastest')

for _ in range(10):
    tim.penup()
    tim.goto(-200, y)
    for _ in range(10):
        draw_line()
    y += 50


screen = t.Screen()
screen.exitonclick()
