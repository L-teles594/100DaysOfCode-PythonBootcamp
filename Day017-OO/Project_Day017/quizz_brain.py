import html


class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f'Q.{self.question_number}: {q_text}'

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, q_answer, current_q):
        if q_answer.lower() == current_q.answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {current_q.answer}')
        print(f'You current score is: {self.score}/{self.question_number}.')
        print('\n')

