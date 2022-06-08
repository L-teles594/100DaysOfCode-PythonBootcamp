from turtle import Screen
from states import States
from score import Score

screen = Screen()
screen.title('U.S.A States Game')
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

states = States()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()

    guess = screen.textinput(f'States Correct {score.score}/{len(states.states)}', "What's another state name?").capitalize()
    for state in states.states:
        if state.name == guess:
            state.goto(state.pos())
            state.write(f'{state.name}')
            score.increase()
            if score.is_over():
                game_is_on = False

screen.exitonclick()