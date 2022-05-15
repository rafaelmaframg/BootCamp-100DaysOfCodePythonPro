from quiz_brain import QuizBrain
from question_model import Question
import json

question_bank = []
with open("data.json", "r") as r:
    question_data = json.load(r)
    question_data = question_data['results']
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.nex_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

