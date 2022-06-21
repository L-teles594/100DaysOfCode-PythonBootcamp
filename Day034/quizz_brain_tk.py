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

    def check_answer(self, q_answer):
        if q_answer == self.current_question.answer:
            self.score += 1
            return True
        return False
