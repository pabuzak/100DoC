from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

### my take on the question - .values() might return the order of items randomly (after python 3.7)
# question_bank = []
# for n in question_data:
#     text, answer = n.values()
#     question_bank.append(Question(text, answer))


question_bank = []
for n in question_data:
    text, answer = n["text"], n["answer"]
    question_bank.append(Question(text, answer))



q = QuizBrain(question_bank)

while q.still_has_questions() is True:
    q.next_question()







