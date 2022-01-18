#----------------------------------------------------------------------------
# File name   : 6_hangman.py
# Created By  : Heesoo Lim
# Created Date: 18/01/2022
# ---------------------------------------------------------------------------

import random
import os
import re

# clear the console
clear = lambda: os.system('clear')
# list of the words
words = ['affix', 'avenue', 'awkward', 'beekeeper', 'boggle', 'cobweb', 'cycle', 'disavow', 'duplex', 'equip', 'exodus', 'funny', 'galaxy', 'gossip', 'icebox', 'injury', 'ivory', 'jackpot', 'jelly', 'jockey', 'joking', 'joyful', 'jumbo', 'kayak', 'khaki', 'kiosk', 'lengths', 'lucky', 'luxury', 'lymph', 'nightclub', 'onyx', 'ovary', 'pajama', 'pneumonia', 'pshaw', 'puppy', 'scratch', 'staff', 'stretch']
# list of the hangman status
hangman_status = ["""

       _____
      |     |
      |    
      |   
      |     
      |    
  ____|____
""","""

       _____
      |     |
      |    (_)
      |   
      |     
      |    
  ____|____
""", """

       _____
      |     |
      |    (_)
      |     |
      |     |
      |    
  ____|____
""", """

       _____
      |     |
      |    (_)
      |    /|
      |     |
      |    
  ____|____
""", """

       _____
      |     |
      |    (_)
      |    /|\\
      |     |
      |    
  ____|____
""", """

       _____
      |     |
      |    (_)
      |    /|\\
      |     |
      |    /
  ____|____
""", """

       _____
      |     |
      |    (_)
      |    /|\\
      |     |
      |    / \\
  ____|____
"""]

# print the welcome message
print("""
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              

Welcome to Hangman!
  
""")
input("Type any letter to start the game.")

# print the status of hangman and previous wrong guess
def print_status(status_number, blank_word, prev_guess):
  print(f"""{hangman_status[hangman_status_number]}
  Incorrect guess: {', '.join(prev_guess)}

  {' '.join(blank_word)}
  """)

# clear the console
clear()

# put the answer word in the array
answer = [char for char in random.choice(words)]
# fill the list with the blanks
blank_word = ["_"] * len(answer)
# declare the empty list of previous guess list
prev_guess = []

# amount of score to deduct when the user input the wrong guess
score_partial = round(100 / len(answer))
# initial status of hangman (=number of wrong guess)
hangman_status_number = 0

while hangman_status_number < len(answer):
  # clear the console
  clear()
  # if the user successfully guessed every letter
  if "_" not in blank_word:
    print("You won!")
    break
  
  # print the status of the hangman and the word
  print("Type a letter to find the word.")
  print_status(hangman_status_number, blank_word, prev_guess)

  # get the user guess input
  guess = input("Your guess: ").lower()

  # only if the user typed a single letter
  if re.match('([a-zA-Z])', guess) and len(guess) == 1:
    is_correct = False

    for n in range(len(answer)):
      if answer[n] == guess:
        blank_word[n] = guess
        is_correct = True

    if not is_correct and guess not in prev_guess:
      if hangman_status_number >= len(answer):
        print("Game over")
      else:
        prev_guess.append(guess)
        hangman_status_number += 1
      


clear()
print_status(hangman_status_number, blank_word, prev_guess)
print(f"Answer: {''.join(answer)}\n")
print(f"Your Score: {100 - score_partial * hangman_status_number}/100")