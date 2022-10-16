import html


class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = ""
    
    def still_has_question(self):
        """
        Function To check if the question is the last one of list.

        Returns:
            bool: return True if the question number is less than question list
        """
        return self.question_number < len(self.question_list)
    
    def nex_question(self):
        """
        Function to get the next question and call the function to check the answer
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
    
    def check_answer(self, user_answer, correct_answer):
        """
        Function to check the answer and contabilize the score

        Args:
            user_answer (bool): user answer to check
            correct_answer (str): the correct answer
        """

        if str(user_answer).lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
        