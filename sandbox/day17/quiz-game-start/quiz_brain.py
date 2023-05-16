from html import unescape
class QuizzBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #current_question_text = current_question.text.replace('&quot;', '"')

        current_question_text = unescape(current_question.text)
        user_answer = input(f"Q.{self.question_number}: {current_question_text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        question_list_length = len(self.question_list)
        return self.question_number < question_list_length

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")
