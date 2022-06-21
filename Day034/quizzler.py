from tkinter import *
from quizz_brain_tk import QuizzBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class Interface:
    def __init__(self, quiz: QuizzBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_label.config(padx=50, pady=50)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(150, 125, text='', width=280, font=FONT, fill='black')
        self.canvas.grid(column=0, row=1, columnspan=2)

        false_img = PhotoImage(file='images/false.png')
        true_img = PhotoImage(file='images/true.png')

        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_answer)
        self.false_button.config(padx=50, pady=50)
        self.false_button.grid(column=1, row=2)

        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_answer)
        self.true_button.config(padx=50, pady=50)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        try:
            self.canvas.config(bg='white')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        except IndexError:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question,
                                   text=f'End of the Quizz\nYour final Score: {self.quiz.score}',
                                   fill='green')
            self.window.after(5000, self.window.destroy)

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
