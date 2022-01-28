#----------------------------------------------------------------------------
# File name   : main.py
# Created By  : Heesoo Lim
# Created Date: 28/01/2022
# ---------------------------------------------------------------------------

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# generate a list of questions from data
questions = []
for q in question_data:
    new_question = Question(q["text"], q["answer"])
    questions.append(new_question)


# instantiate the QuizBrain object passing the question list
quiz_brain = QuizBrain(questions)


# repeat the quiz until it ends
while not quiz_brain.is_quiz_over():
    answer = quiz_brain.ask_question()
    quiz_brain.is_answer_correct(answer)
    quiz_brain.next_question()
    quiz_brain.display_score(False)

# display the final score
quiz_brain.display_score(True)



