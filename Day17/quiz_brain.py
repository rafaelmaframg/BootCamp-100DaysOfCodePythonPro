class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number =  0
        self.question_list = question_list
    
    def nex_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)")
        



#TODO asking the questions
#TODO checking if the answer was correct
#TODO checking if we're the end of the quiz
