from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))


quiz = QuizzBrain(question_bank)

quiz.next_question()
