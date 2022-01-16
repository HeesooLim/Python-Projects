#----------------------------------------------------------------------------
# File name   : 5_password-generator.py
# Created By  : Heesoo Lim
# Created Date: 16/01/2022
# ---------------------------------------------------------------------------

import random

print("""
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | LOCK |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
""")

print("Welcome to password generator!\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_of_letters = int(input("How many letters do you want to have in your password?\n"))
num_of_symbols = int(input("How many symbols do you want?\n"))
num_of_numbers = int(input("How many numbers do you want?\n"))

pw_len = num_of_letters + num_of_symbols + num_of_numbers

selected_chars = []

for n in range(num_of_letters):
  selected_chars.append(letters[random.randint(0, len(letters) - 1)])
for n in range(num_of_numbers):
  selected_chars.append(numbers[random.randint(0, len(numbers) - 1)])
for n in range(num_of_symbols):
  selected_chars.append(symbols[random.randint(0, len(symbols) - 1)])

password = ""

for n in range(pw_len):
  index = random.randint(0, len(selected_chars) - 1)
  selected_char = selected_chars[index]
  password += selected_char
  selected_chars.remove(selected_char)


print(f"\nYour password: {password}\n")


