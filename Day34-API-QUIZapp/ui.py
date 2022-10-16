from tkinter import *
import os
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
PATH = os.path.dirname(__file__)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.lbl_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, width=280, text="",
                                            font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file=os.path.join(PATH, "images/true.png"))
        img_false = PhotoImage(file=os.path.join(PATH, "images/false.png"))
        self.right = Button(image=img_true, highlightthickness=0, borderwidth=0, command=lambda: self.click(True))
        self.right.grid(row=2, column=0)

        self.false = Button(image=img_false, command=lambda: self.click(False))
        self.false.configure(highlightthickness=0, borderwidth=0)
        self.false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def click(self, anwser: bool):
        if self.quiz.still_has_question():
            check = self.quiz.check_answer(anwser, self.quiz.current_question.answer)
            if check:
                self.canvas.configure(bg="green")
            else:
                self.canvas.configure(bg="red")
            self.window.after(1000, self.get_next_question)
            self.lbl_score.configure(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.configure(bg="white")
        question = self.quiz.nex_question()
        self.canvas.itemconfig(self.text, text=question)
