#----------------------------------------------------------------------------
# File name   : 3_treasure-game.py
# Created By  : Heesoo Lim
# Created Date: 14/01/2022
# ---------------------------------------------------------------------------


print("""



    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~

""")

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

# Q: Do you want to enter the forest? yes/no
enter_forest = input("You just got to the forest. Do you want to enter? Answer 'yes' or 'no'\n")

# forest: yes
if enter_forest == "yes":

  # Q: Do you want to explore the lake? yes/no
  lake = input("You now got to a huge lake with an island in the middle. Do you want to explore the island? Answer 'yes' or 'no'\n")

  # forest: yes / lake: yes
  if lake == "yes":

    # Q: Choose one of the rooms red/blue/black
    treasure = input("You arrive at the island. There are 3 rooms and you can choose one of them. Choose one from 'red', 'blue', 'black'\n")

    # forest: yes / lake: yes / room: red
    if treasure == 'red':
      print("You entered a room of monsters. Game Over.")

    # forest: yes / lake: yes / room: blue
    elif treasure == 'blue':
      print("Congratulations! you found a room of treasures!")

    # forest: yes / lake: yes / room: black
    elif treasure == 'black':
      print("You found a room of (poisonous) food and you ate the food. Game Over.")
    else:
      print("Please retry and enter a valid answer.")

  # forest: yes / lake: no
  elif lake == "no":
    print("You decided to go back home and nothing happened.")
  else:
    print("Please retry and enter a valid answer.")


# forest: no
elif enter_forest == "no":

  # Q: Type 'wait' to wait
  wait = input("You decided not to enter the forest. Type 'wait' to wait for the taxi\n")
  
  # forest: no / wait: wait
  if wait == "wait":
    print("You arrived home and nothing happened.")
  else:
    print("You arrived home by foot and nothing happened.")
else:
  print("Please retry and enter a valid answer.")