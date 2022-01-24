#----------------------------------------------------------------------------
# File name   : 11_number-guessing.py
# Created By  : Heesoo Lim
# Created Date: 23/01/2022
# ---------------------------------------------------------------------------

import random

print("""
    _   __                __               
   / | / /_  ______ ___  / /_  ___  _____  
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  
 / /|  / /_/ / / / / / / /_/ /  __/ /      
/_/_|_/\__,_/_/ /_/ /_/_.___/\___/_/       
  / ____/_  _____  __________(_)___  ____ _
 / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/
/ /_/ / /_/ /  __(__  |__  ) / / / / /_/ / 
\____/\__,_/\___/____/____/_/_/ /_/\__, /  
  / ____/___ _____ ___  ___       /____/   
 / / __/ __ `/ __ `__ \/ _ \               
/ /_/ / /_/ / / / / / /  __/               
\____/\__,_/_/ /_/ /_/\___/                   

""")

print("Welcome to number guessing game!\n")

# choose the game level
level = input("choose the difficulty level you want (easy/hard): ")

# initial chance is 5
chance = 5

# if the level is easy, chance will be 10
if level == 'easy':
  chance = 10

# select a random number
answer = random.randint(1, 100)

# number of trial is initially 0
trial = 0

print("\nI have a number between 1 and 100. Try to guess!\n")

for i in range(chance):
  print(f"\nchance left: {chance - trial}\n")
  guess = int(input("Your guess: "))
  
  diff = answer - guess

  if diff < 0:
    if diff < -30:
      print("\nThat was too high")
    elif diff < -10:
      print("\nThat was high")
    else:
      print("\nThat was a bit higher")
  elif diff > 0:
    if diff > 30:
      print("\nThat was too low")
    elif diff > 10:
      print("\nThat was low")
    else:
      print("\nThat was a bit lower")
  else:
    print(f"\nBingo! the answer was {answer}")
    break

  # if the user runs out of chance
  if trial == chance - 1:
    print(f"\nYou run out of chances.. the answer was {answer}")
  
  trial += 1

