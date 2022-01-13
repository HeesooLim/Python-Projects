print("Welcome to the bill calculator!")
print("Please enter following information..\n")

# initial value of the bill, tip and split
bill = 0
tip = 0
split = 0

# ask for the total bill input until the correct value is entered
while True: 
  bill = float(input("Total bill: $"))
  # bill should be greater than 0
  if bill > 0:
    break
# ask for the tip input until the correct value is entered
while True: 
  tip = float(input("Tip percentage to give: "))
  # tip should be between 0 and 100
  if tip >= 0 and tip <= 100:
    break
# ask for the split input until the correct value is entered
while True: 
  split = int(input("Number of people to split the bill: "))
  # number of people to split should be greater than or equal to 0
  if split >= 0:
    break

# calculate the bill for each
total = (bill + bill * tip/100) / split

print(f"Bill for each person: ${total}")
print("Thank you for using our program!")