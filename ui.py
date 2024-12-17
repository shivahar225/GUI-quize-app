from tkinter import *
from quize_brain import Quizebrain

THEME_COLOR = "#375362"

class Quizinterface:

    def __init__(self,quize_brain: Quizebrain):
        self.quize = quize_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question text",
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.true_button = Button(text="true", highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(text="false",highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

        self.get_next_question()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quize.still_has_question():
            self.score_label.config(text=f"score:{self.quize.score}")
            q_text = self.quize.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have reached the end of the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        is_right = self.quize.check_answer("true")

    def false_pressed(self):
        is_right = self.quize.check_answer("false")

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

