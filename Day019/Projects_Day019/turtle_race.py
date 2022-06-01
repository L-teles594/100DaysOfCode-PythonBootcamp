from turtle import Turtle, Screen


def start_running(objcts):
    from random import randint
    while True:
        for obj in objcts:
            run = randint(1, 10)
            obj.forward(run)
            if obj.xcor() >= 230:
                return obj


def did_player_win(choice, obj):
    if choice == obj.fillcolor():
        print('You turtle win!')
    else:
        print('Your turtle lose! try again.')


# Setting up the screen
screen = Screen()
screen.setup(width=500, height=400)
colors = ('red', 'blue', 'yellow', 'purple', 'green', 'orange')
positions = (-70, -40, -10, 20, 50, 80)
turtles = list()

# Setting up The turtles and their initial position
for i in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[i])
    new_turtle.pendown()
    turtles.append(new_turtle)


# Making the screen listen to the running events
screen.listen()
player_bet = screen.textinput(title='Your choice', prompt='Choose your turtle by the color: ')
wining_turtle = start_running(turtles)
did_player_win(player_bet, wining_turtle)
screen.bye()
