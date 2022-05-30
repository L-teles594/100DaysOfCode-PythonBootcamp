from question_model import Question
from data import question_data
from quizz_brain import QuizzBrain

question_bank = []

for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)

quiz = QuizzBrain(question_bank)

while quiz.still_haas_question():
    quiz.next_question()

print("You've complete the quiz!")
print(f'Your final score was {quiz.score}/{quiz.question_number}')
