from question_model import Question
from quize_brain import Quizebrain
from data import question_data
from ui import Quizinterface

question_bank = []
for question in question_bank:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

quize = Quizebrain(question_bank)
quize_ui= Quizinterface(quize)
question = question_data

print("you are completed the quize")
print(f"your final score{quize.sco
