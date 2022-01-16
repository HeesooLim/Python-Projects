#----------------------------------------------------------------------------
# File name   : 4_rock-paper-scissors.py
# Created By  : Heesoo Lim
# Created Date: 16/01/2022
# ---------------------------------------------------------------------------


import random

# print Ascii art
print("""
 .d88b.  8888b. 88888b.d88b.  .d88b. .d8888b  
d88P"88b    "88b888 "888 "88bd8P  Y8b88K      
888  888.d888888888  888  88888888888"Y8888b. 
Y88b 888888  888888  888  888Y8b.         X88 
 "Y88888"Y888888888  888  888 "Y8888  88888P' 
     888                                      
Y8b d88P                                      
 "Y88P" 
 """)
# display an instruction
print("""
Welcome to Rock Paper scissors game!

Rock: 1
Paper: 2
scissors: 3
""")

# get an input from the user
choice = int(input("Please type a number: "))

rock = """
      ,--.--._
  ---" _, \___)
      / _/____)
      \//(____)
  ---\     (__)
      `-----
"""

paper = """
         _
     _  / |
    / \ | | /\
    \ \| |/ /
     \ Y | /___
   .-.) '. `__/
   (.-.   / /
       | ' |
       |___|
      [_____]
      |     |
"""

scissors = """
        .-.  _
        | | / )
        | |/ /
       _|__ /_
      / __)-' )
      \  `(.-')
      > ._>-'
      / \/
"""

# store the ascii art in the array
asciis = [rock, paper, scissors]

# select a random number between 1 and 3
opponent = random.randint(1, 3)

# print the choice of the user and the opponent
print(f"You: \n{asciis[choice - 1]}")
print(f"Opponent: \n{asciis[opponent - 1]}")

# if the same, draw
if choice == opponent:
  print("Result: Draw")
# otherwise, print the result accordingly
else:
  if choice == 1:
    if opponent == 2:
      print("Result: You lose")
    if opponent == 3:
      print("Result: You win")
  if choice == 2:
    if opponent == 3:
      print("Result: You lose")
    if opponent == 1:
      print("Result: You win")
  if choice == 3:
    if opponent == 1:
      print("Result: You lose")
    if opponent == 2:
      print("Result: You win")
