#----------------------------------------------------------------------------
# File name   : quiz_brain.py
# Created By  : Heesoo Lim
# Created Date: 28/01/2022
# ---------------------------------------------------------------------------


import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        # shuffle the order of the questions
        random.shuffle(self.question_list)
        self.score = 0
        self.question_number = 0

    # ask the questions
    def ask_question(self):
        curr_question = self.question_list[self.question_number].question
        answer = input(f"Q{self.question_number + 1}. {curr_question} (t/f): ")

        # if the answer is 't', return 'True'
        if answer.lower() == 't':
            return 'True'
        # if the answer is 'f', return 'False'
        elif answer.lower() == 'f':
            return 'False'
        else:
            return answer

    # check if the answer was correct
    def is_answer_correct(self, answer):
        curr_answer = self.question_list[self.question_number].answer
        # Compare the answer and if it's correct, add 1 to score and return True
        if curr_answer == answer:
            print("That's correct!")
            self.score += 1
            return True
        return False

    # move to the next question
    def next_question(self):
        # add 1 to the question number only when it does not exceed the number of questions
        if self.question_number <= len(self.question_list):
            self.question_number += 1

    # check if quiz ended
    def is_quiz_over(self):
        # return true if current question number is greater than or equal to the number of questions
        if self.question_number >= len(self.question_list):
            return True
        return False

    # display current score
    def display_score(self, is_final):
        # if the user wants to print the final score, print with the total number of questions
        if is_final:
            print(f"Your final score: {self.score}/{len(self.question_list)}")
        else:
            print(f"Score: {self.score}\n")
