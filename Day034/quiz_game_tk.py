from question_model_tk import Question
from data_tk import question_data
from quizz_brain_tk import QuizzBrain
from quizzler import Interface

question_bank = []

for data in question_data:
    question = Question(data['question'], data['correct_answer'])
    question_bank.append(question)

quiz = QuizzBrain(question_bank)
interface = Interface(quiz)
