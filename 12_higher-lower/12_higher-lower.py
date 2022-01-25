import ascii
import random
import data
import os

# print game logo
print(ascii.logo)

# function to clear the console
clear = lambda: os.system('clear')
score = 0

# generate the list of data to compare
def generate_comp_list():
  # create an empty list
  comp_list = []
  # append the list with the random data
  comp_list.append(random.choice(data.info))
  comp_list.append(random.choice(data.info))
  # change the second element if the first and second elements are identical
  while comp_list[0] == comp_list[1]:
    comp_list[1] = random.choice(data.info)
  # return the list
  return comp_list

start = input("Welcome to higher lower. Type 'y' to start the game!")

if start == 'y':
  while True:
    clear()
    comparisons = generate_comp_list()

    print("Guess who has higher number of follower!\n")
    print(f"Current score: {score}\n")
    
    comp_a = comparisons[0]
    comp_b = comparisons[1]

    print(f"A: {comp_a['name']}, {comp_a['description']}, from {comp_a['country']}")
    print(f"B: {comp_b['name']}, {comp_b['description']}, from {comp_b['country']}\n")

    # get the higher value
    higher_value = max(comp_a['follower_count'], comp_b['follower_count'])

    # get the data with the higher follower count
    if comp_a['follower_count'] == higher_value:
      higher_dict = comp_a
      answer = 'a'
    else:
      higher_dict = comp_b
      answer = 'b'

    user_answer = input("Type 'a' or 'b': ")

    # if correct, regenerate the comparison list and add score
    if answer == user_answer:
      comparisons = generate_comp_list()
      score += 1
    else:
      print("_____________________________________\n")
      print(f"Final score: {score}")
      print(f"The answer was {higher_dict['name']} with {higher_value} followers.")
      print("_____________________________________\n")

      restart = input("Do you want to play again? type 'y' to restart.\n")

      if restart != 'y':
        break
      else:
        score = 0