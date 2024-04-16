class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.q_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        num = self.question_number
        q = self.q_list[num]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {q.text} (True/False)?: ")

        


