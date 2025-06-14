from question_model import question
from data import question_data
from quiz_brain import quizbrain
import time
question_bank = []


for item in question_data:
    ques_text = item["question"]
    ques_answer = item["answer"]
    new_question = question(ques_text, ques_answer)
    question_bank.append(new_question)


quiz = quizbrain(question_bank)
for i in question_bank:

    quiz.next_ques()

    quiz.q_number += 1
print(f"score is:{quiz.score}/{quiz.q_number}")
