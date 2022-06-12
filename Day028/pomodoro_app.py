from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
time = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_count():
    global marks, reps, time
    screen.after_cancel(time)
    timer.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    marks = ''
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer.config(text='Long Rest', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    if reps % 2 == 0:
        timer.config(text='Short Rest', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text='Work Time', fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    from math import floor
    global marks, time

    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{count_min:0>2}:{count_sec:0>2}')
    if count > 0:
        time = screen.after(1000, count_down, count - 1)
    else:
        start_count()
        for _ in range(floor(reps/2)):
            marks += '✔'
        done.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Pomodoro App')
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)


timer = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer.grid(column=2, row=1)

done = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
done.grid(column=2, row=4)

start_btn = Button(text='Start', command=start_count, bg=YELLOW, highlightthickness=0)
start_btn.grid(column=1, row=3)

reset_btn = Button(text='Reset', command=reset_count, bg=YELLOW, highlightthickness=0)
reset_btn.grid(column=3, row=3)

screen.mainloop()
