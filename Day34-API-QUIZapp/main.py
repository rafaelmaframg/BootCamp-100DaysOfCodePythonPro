import requests
from quiz_brain import QuizBrain
from question_model import Question
from ui import QuizInterface


question_bank = []

payload = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=payload)
response = response.json()

question_data = response['results']
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

