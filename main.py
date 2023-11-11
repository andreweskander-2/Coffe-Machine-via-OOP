from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Defining Objects and Variables
coffemaker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
items = menu.get_items()

#Repeat the program so the following user can order
next_order = True
while next_order:

    #Welcoming Message and Taking Customer input
    print (f"\nWelcome to our Fab Coffee Machine!")
    selection = input(f"\nPlease enter your choice of a drink. The available options are {items}\n").lower()

    #Check special inputs such as: if user asked for report or to turn off the machine
    if selection == 'report':
        coffemaker.report()
        money.report()
    elif selection == 'off':
        exit()

    #Payment and Drink Preparation
    else:
        drink = menu.find_drink(selection)
        if drink != None:
            #Check for sufficient resources
            if coffemaker.is_resource_sufficient(drink):
                print(f"Your {drink.name} costs ${drink.cost}...")
                #Check for sufficient payment
                if money.make_payment(drink.cost):
                    coffemaker.make_coffee(drink)
                else:
                    print("Please Try Again!")
            else:
                print("Insufficient resources.. Please Try Again Later!")


