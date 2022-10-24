from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
the_menu = Menu()

while True:
    prompt = input(f'​What would you like? ({the_menu.get_items()}): ')
    if prompt in [':q', 'quit', 'exit', 'stop']:
        break
    elif prompt == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = the_menu.find_drink(prompt)    
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)