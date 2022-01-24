#----------------------------------------------------------------------------
# File name   : 10_black-jack.py
# Created By  : Heesoo Lim
# Created Date: 23/01/2022
# ---------------------------------------------------------------------------

import os
import random

# function to clear the console
clear = lambda: os.system('clear')

print("""
  .------..-----..-----..-----..-----..-----..-----..-----..-----.
  |B.--. |L.--. |A.--. |C.--. |K.--. |J.--. |A.--. |C.--. |K.--. |
  | :(): | :/\: | (\/) | :/\: | :/\: | :(): | (\/) | :/\: | :/\: |
  | ()() | (__) | :\/: | :\/: | :\/: | ()() | :\/: | :\/: | :\/: |
  | '--'B| '--'L| '--'A| '--'C| '--'K| '--'J| '--'A| '--'C| '--'K|
  `------'`-----'`-----'`-----'`-----'`-----'`-----'`-----'`-----'

                                    
   _   _         _    _         _   
  | |_| |___ ___| |_ |_|___ ___| |_ 
  | . | | .'|  _| '_|| | .'|  _| '_|
  |___|_|__,|___|_,__| |__,|___|_,_|
                  |___|            
""")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
card_number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'K', 'Q']

# draw a new card
def draw_card(card_indexes):
  new_card = random.randint(0, 11)
  card_indexes.append(new_card)
  return new_card

# print the list of cards
def print_cards(card_indexes):
  line = ""
  for n in card_indexes:
    line += " ___ "
  print(line)

  line = ""
  for n in card_indexes:
    line += f"|{card_number[n]}  |"
  print(line)

  line = ""
  for n in card_indexes:
    line += "| /\|"
  print(line)

  line = ""
  for n in card_indexes:
    line += "|_\/|"
  print(line)

  all_cards = [cards[n] for n in card_indexes]
  cards_sum = sum(all_cards)

  # print the sum of the numbers
  print(f"\nSum of cards: {cards_sum}\n")

# print the dealer and the user's card
def print_summary(user_cards, dealer_cards):
  print("Dealer's cards:")
  print_cards(dealer_cards)
  
  print("Your cards:")
  print_cards(user_cards)

# let the dealer draw card
def complete_dealer_card(dealer_cards_index):
  # get the card numbers using the index
  dealer_cards = [cards[n] for n in dealer_cards_index] 
  # check if it contains ace
  contains_ace = 11 in dealer_cards
  # get the sum of the numbers
  dealer_sum = sum(dealer_cards)
  # if ace is included, ace is 1 if current sum is greater than 21
  if dealer_sum > 21 and contains_ace:
    dealer_sum - 10

  # draw a new card if the sum of the card is less than 17
  while dealer_sum <= 16:
    new_card = draw_card(dealer_cards_index)
    dealer_sum += cards[new_card]

    # if the new card is ace
    if new_card == 0:
      # ace is 1 if current sum is greater than 21
      if dealer_sum > 21:
        dealer_sum - 10   

  return dealer_sum

answer = input("Welcome! type 'y' to start the game.\n")

user_sum = 0

if answer == 'y':
  clear()
  # add 2 cards(index) to both user and dealer
  user_card_indexes = [random.randint(0, 11) for n in range(2)]
  dealer_card_indexes = [random.randint(0, 11) for n in range(2)]

  user_sum = sum([cards[i] for i in user_card_indexes])

  # print cards
  print_summary(user_card_indexes, dealer_card_indexes)

  # ask the user if he/she wants to stand or draw
  action = input("Type 's' to stand and 'd' to draw more card.\n")

  while action == 'd':
    clear()
    
    # user draws a card
    new_card = draw_card(user_card_indexes)
    user_sum += cards[new_card]

    # if the new card is ace
    if new_card == 0:
      # ace is 1 if current sum is greater than 21
      if user_sum > 21:
        user_sum - 10  

    # print cards
    print_summary(user_card_indexes, dealer_card_indexes)
    # if the user's sum is over 21 (LOSE)
    if user_sum > 21:
      clear()      
      print("You lose..\n\n========= SUMMARY =========\n")
      print_summary(user_card_indexes, dealer_card_indexes)
      break
    elif user_sum == 21:
      clear()
      print("You win!\n\n========= SUMMARY =========\n")
      print_summary(user_card_indexes, dealer_card_indexes)
      break
    
    action = input("Type 's' to stand and 'd' to draw more card.\n")

  if action == 's':
    clear()
    dealer_sum = complete_dealer_card(dealer_card_indexes)

    if user_sum > dealer_sum:
      if user_sum > 21:
        print("You lose..\n\n========= SUMMARY =========\n")
      else:
        print("You win!\n\n========= SUMMARY =========\n")
    elif user_sum < dealer_sum:
      if dealer_sum > 21:
        print("You win!\n\n========= SUMMARY =========\n")
      else:
        print("You lose..\n\n========= SUMMARY =========\n")
    else:
      print("Draw\n\n========= SUMMARY =========\n")

    print_summary(user_card_indexes, dealer_card_indexes)
        
      
 
    


