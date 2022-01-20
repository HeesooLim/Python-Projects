#----------------------------------------------------------------------------
# File name   : 8_secret-auction.py
# Created By  : Heesoo Lim
# Created Date: 20/01/2022
# ---------------------------------------------------------------------------


import os

# function to clear the console
clear = lambda: os.system('clear')


# enpty dictionary to store the bidder information
bidders = {}

# store the previous name and bid
prev_name = ""
prev_bid = 0
# store the name and the bid of the winner
winner_name = ""
winner_bid = 0

while True:
  # clear the console
  clear()
  print("""
 __.             ,  
(__  _  _.._. _ -+- 
.__)(/,(_.[  (/, |  
                    
.__.       ,        
[__]. . _.-+-* _ ._ 
|  |(_|(_. | |(_)[ )


Welcome to the Secret Auction!       
""")
  name = input("Please type your name:\n")
  bid = int(input("Please type your bid:\n$"))

  # if the entered bid is greater than current winner's bid
  if bid > winner_bid:
    # assign the new name and the bid
    winner_name = name
    winner_bid = bid

  # assign the entered name to the previous name and bid
  prev_name = name
  prev_bid = bid

  answer = input("\nType 'yes' if there are other bidders. Otherwise, type any letters.\n").lower()
  bidders[name] = bid
  # if the user didn't input 'yes', stop the program
  if answer != "yes":
    clear()
    print(f"Winner: {winner_name} with a bid of ${winner_bid}")
    break
