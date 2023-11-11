from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffemaker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
items = menu.get_items()

next_order = True
while next_order:
    print (f"\nWelcome to our Fab Coffee Machine!")
    selection = input(f"\nPlease enter your choice of a drink. The available options are {items}\n").lower()

    if selection == 'report':
        coffemaker.report()
        money.report()
    elif selection == 'off':
        exit()
    else:
        drink = menu.find_drink(selection)
        if drink != None:
            if coffemaker.is_resource_sufficient(drink):
                print(f"Your {drink.name} costs ${drink.cost}...")
                if money.make_payment(drink.cost):
                    coffemaker.make_coffee(drink)
                else:
                    print("Please Try Again!")
            else:
                print("Insufficient resources.. Please Try Again Later!")


