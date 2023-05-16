from question_model import Question
#from data import question_data
from quiz_brain import QuizzBrain
from open_trivia_data import question_data

question_bank = []

for question in question_data:
    # Could use open trivia database to generate new random questions from (https://opentdb.com/)
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
