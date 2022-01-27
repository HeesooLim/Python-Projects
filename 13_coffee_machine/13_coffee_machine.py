# ----------------------------------------------------------------------------
# File name   : 13_coffee_machine.py
# Created By  : Heesoo Lim
# Created Date: 27/01/2022
# ---------------------------------------------------------------------------

import data
import menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

more_drink = True

store_menu = menu.Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while more_drink:
    # clear()
    print(data.ascii)
    print("What would you like to have? ")
    menu_name = input(store_menu.get_items())

    if menu_name == "off":
        print("machine turned off.")
        more_drink = False
    elif menu_name == "report":
        coffee_maker.report()
        money_machine.report()
        more_drink = True
    else:
        menu_item = store_menu.find_drink(menu_name)
        if menu_item is None:
            print("Menu not found.")
            break
        if coffee_maker.is_resource_sufficient(menu_item):
            print(f"{menu_item.name} is ${menu_item.cost}")
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
            else:
                print("money is not sufficient.\nPaid:")
                break

            more_drink = input("do you want more drink? Type 'y' to get more drink: ") == 'y'