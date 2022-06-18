from tkinter import *
from pandas import read_csv, DataFrame
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
actual_card = {}
words = {}

# CREATING THE WORDS DICTIONARY FROM CSV USING PANDAS FUNCTION READ_CSV
try:
    data = read_csv('data/french_words.csv')
except FileNotFoundError:
    origin_data = read_csv('data/french_words.csv')
    words = origin_data.to_dict(orient='records')
else:
    words = data.to_dict(orient='records')


# FLIP CARD FUNCTION
def flip_card():
    canvas.itemconfig(front_image, image=card_back)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=actual_card['English'], fill='white')


# GENERATE CARD FUNCTION
def card_gen():
    global actual_card, flip_timer
    screen.after_cancel(flip_timer)
    actual_card = choice(words)
    canvas.itemconfig(front_image, image=card_front)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=actual_card['French'], fill='black')
    flip_timer = screen.after(3000, func=flip_card)


# LEARNED CARD FUNCTION
def is_known():
    words.remove(actual_card)
    new_data = DataFrame(words)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    card_gen()


# SETTING SCREEN UP
screen = Tk()
screen.title('Flashy')
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, func=flip_card)

# SETTING THE IMAGES
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
wrong_image = PhotoImage(file='images/wrong.png')
right_image = PhotoImage(file='images/right.png')

# SETTING TEH CANVAS UP
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# SETTING THE BUTTONS UP
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=card_gen)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

card_gen()
screen.mainloop()
