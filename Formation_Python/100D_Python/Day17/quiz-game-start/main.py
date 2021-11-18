from question_model import Question
from data import var  # ,question_data,
from quiz_brain import QuizBrain

question_bank = []
for dict_question in var:
    new_question = Question(dict_question.get("question"), dict_question.get("correct_answer"))
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
