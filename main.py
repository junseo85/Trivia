from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for item in question_data:
    question = item["question"]
    answer = item["correct_answer"]
    new_question = Question(question,answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

#print(question_bank[0].text)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
