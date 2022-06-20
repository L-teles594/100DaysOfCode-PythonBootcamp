from tkinter import *

BACKGROUND = '#9EB23B'
FONT = ('Ariel', 20, 'bold')


def get_quote():
    import requests
    response = requests.get(url='https://api.kanye.rest')
    quote = response.json()['quote']
    set_quote_on_gui(quote)


def set_quote_on_gui(quote):
    canvas.itemconfig(message, text=quote)


window = Tk()
window.title('Kenye Says...')
window.config(padx=50, pady=50, bg=BACKGROUND)

kanye_face = PhotoImage(file='images/kanye.png')
bg_ballon = PhotoImage(file='images/background.png')

canvas = Canvas(width=300, height=414, bg=BACKGROUND, highlightthickness=0)
canvas.create_image(150, 207, image=bg_ballon)
message = canvas.create_text(150, 207, text='', width=250, fill='white', font=FONT)
canvas.grid()

kanye_quote = Button(image=kanye_face, bg=BACKGROUND, highlightthickness=0, command=get_quote)
kanye_quote.grid()

get_quote()
window.mainloop()
