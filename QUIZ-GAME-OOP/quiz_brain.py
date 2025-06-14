
class quizbrain:
    def __init__(self, assign_ques):
        self.assign_ques = assign_ques
        self.q_number = 0
        self.score = 0

    def next_ques(self):
        ques_is = self.assign_ques[self.q_number]

        user_answer = input(
            f"Q{self.q_number+1}:{ques_is.context}(True/False)\n Answer:")

        if user_answer.lower() == ques_is.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {ques_is.answer}")
