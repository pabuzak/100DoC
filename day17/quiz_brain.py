class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        num = self.question_number
        q = self.q_list[num]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {q.text} (True/False)?: ")
        self.check_answer(user_input, q.answer)

    def check_answer(self, input, answer):
        if input.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


