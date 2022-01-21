#----------------------------------------------------------------------------
# File name   : 9_calculator.py
# Created By  : Heesoo Lim
# Created Date: 21/01/2022
# ---------------------------------------------------------------------------

print("""
  _____________________
  |  _________________  |
  | |              0. | |
  | |_________________| |
  |  ___ ___ ___   ___  |
  | | 7 | 8 | 9 | | + | |
  | |___|___|___| |___| |
  | | 4 | 5 | 6 | | - | |
  | |___|___|___| |___| |
  | | 1 | 2 | 3 | | x | |
  | |___|___|___| |___| |
  | | . | 0 | = | | / | |
  | |___|___|___| |___| |
  |_____________________|

Welcome to calculator
""")

print("addition:        +")
print("subtraction:     -")
print("multiplication:  *")
print("division:        /\n")

    
def add(num1, num2):
  return num1 + num2
    
def subtract(num1, num2):
  return num1 - num2
    
def multiply(num1, num2):
  return num1 * num2
    
def devide(num1, num2):
  return num1 / num2

# operations dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devide
}

first_number = int(input("First number to caluclate: "))

while True:
  operation = input("Please choose an operation: ")
  second_number = int(input("next number to calculate: "))
  
  # calculate and print the result
  result = operations[operation](first_number, second_number)
  print(f"{first_number} {operation} {second_number} = {result}\n")

  answer = input(f"'y' to continue calculating with {result} \n'n' to start a new calculation \nother key to finish the program:\n")

  # if the user continues calculating with the result
  if answer == 'y':
    # assign the result value to the first number
    first_number = result
  # start a new calculation
  elif answer == 'n':
    first_number = int(input("First number to caluclate: "))
  else:
    break

  
