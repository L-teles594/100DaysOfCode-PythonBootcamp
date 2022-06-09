from turtle import Turtle
import pandas

DATA = pandas.read_csv('50_states.csv')
FONT = ('Courier', 6, 'boldp-´=p')


class States:
    def __init__(self):
        self.states = []
        self.create_state()
        self.guessed_states = []

    def create_state(self):
        for row in DATA.values:
            new_state = Turtle()
            new_state.name = row[0]
            new_state.shape('turtle')
            new_state.penup()
            new_state.hideturtle()
            new_state.goto(row[1], row[2])
            self.states.append(new_state)

    def get_guessed(self, guess):
        self.guessed_states.append(guess)