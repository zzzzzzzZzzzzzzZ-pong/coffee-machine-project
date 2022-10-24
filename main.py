from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
the_menu = Menu()

print(f'Here are all the stuff we got: {the_menu.get_items()}')