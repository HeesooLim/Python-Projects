# ----------------------------------------------------------------------------
# File name   : 13_coffee_machine.py
# Created By  : Heesoo Lim
# Created Date: 27/01/2022
# ---------------------------------------------------------------------------

import data
import os

# function to clear the console
clear = lambda: os.system('clear')

curr_money = 0
curr_water = data.resources['water']
curr_milk = data.resources['milk']
curr_coffee = data.resources['coffee']

menu = data.MENU


def is_res_enough(resource_name, curr_resource, resource_to_compare):
    """Check if current resource is greater than required resource"""
    if curr_resource < resource_to_compare:
        print(f"There is not enough {resource_name}.")
        return False
    return True


def insert_coins():
    """Ask the user the number of coins inserted and return the paid amount"""
    toonies = int(input("\nHow many toonies are you inserting?"))
    loonies = int(input("How many loonies are you inserting?"))
    quarters = int(input("How many quarters are you inserting?"))
    dimes = int(input("How many dimes are you inserting?"))

    return (2 * toonies) + loonies + (0.25 * quarters) + (dimes * 0.1)


def process_coin(_money_paid, _price):
    """Compare the paid amount and cost and return True if paid amount is enough"""
    print(f"\nPaid    : ${_money_paid}")
    print(f"Price   : ${_price}")
    if _money_paid >= _price:
        print(f"Change  : ${round(_money_paid - _price, 2)}")
        return True
    elif _money_paid < _price:
        print("Please insert enough money. Money refunded")
        return False


more_drink = True

while more_drink:
    clear()
    print(data.ascii)
    print("What would you like to have? ")
    coffee_type = input(f"""  1. espresso (${menu['espresso']['cost']})
  2. latte (${menu['latte']['cost']})
  3. cappuccino (${menu['cappuccino']['cost']})
Type the number you want: """)

    if coffee_type == "off":
        print("machine turned off.")
        more_drink = False
    elif coffee_type == "report":
        print(f"Water  : {curr_water}ml")
        print(f"Milk   :  {curr_milk}ml")
        print(f"Coffee : {curr_coffee}g")
        print(f"Money  : ${curr_money}")
        more_drink = False
    else:
        req_water = 0
        req_milk = 0
        req_coffee = 0
        if coffee_type == '1':
            req_water = menu["espresso"]["ingredients"]["water"]
            req_coffee = menu["espresso"]["ingredients"]["coffee"]
            cost = menu["espresso"]["cost"]
        elif coffee_type == '2':
            req_water = menu["latte"]["ingredients"]["water"]
            req_milk = menu["latte"]["ingredients"]["milk"]
            req_coffee = menu["latte"]["ingredients"]["coffee"]
            cost = menu["latte"]["cost"]
        elif coffee_type == '3':
            req_water = menu["cappuccino"]["ingredients"]["water"]
            req_milk = menu["cappuccino"]["ingredients"]["milk"]
            req_coffee = menu["cappuccino"]["ingredients"]["coffee"]
            cost = menu["cappuccino"]["cost"]

        if is_res_enough("water", curr_water, req_water) and is_res_enough("milk", curr_milk,
                                                                           req_milk) and is_res_enough("coffee",
                                                                                                       curr_coffee,
                                                                                                       req_coffee):
            money_paid = insert_coins()
            if process_coin(money_paid, cost):
                curr_money += cost
                curr_water -= req_water
                curr_milk -= req_milk
                curr_coffee -= req_coffee
                print("\nHere is your drink. Enjoy!")
                more_drink = input("do you want more drink? Type 'y' to get more drink: ") == 'y'
