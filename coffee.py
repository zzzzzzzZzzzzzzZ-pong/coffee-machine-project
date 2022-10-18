import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0

def is_resources_enough(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] >= ingredients[ingredient]:
            resources[ingredient] = resources[ingredient] - ingredients[ingredient]
        if ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, we don't have enough {ingredient}")
            return False
    return True


exit_conditions = [':q', 'quit', 'exit', 'off']
while True:
    coffee_prompt = input('What would you like? (espresso/latte/cappuccino): ')
    if coffee_prompt in exit_conditions:
        break
    elif coffee_prompt == 'help':
        print("""
help - takes you here
report - gives you a report of all ingredients we have left
off - tunrs off the program
            """)
    elif coffee_prompt == 'report':
        print(f"""
Water: {resources.get("water")}ml
Milk: {resources.get("milk")}ml
Coffee: {resources.get("coffee")}g
Money: ${profit}
            """)
    else:
        drink = MENU[coffee_prompt]
        if is_resources_enough(drink["ingredients"]):
            quaters = int(input('How many quaters: ')) * 0.25
            dimes = int(input('How many dimes: ')) * 0.10
            nickles = int(input('How many nickels: ')) * 0.05
            pennies = int(input('How many pennies: ')) * 0.01

            money = quaters + dimes + nickles + pennies
            # print('Getting the ingredients...')
            # time.sleep(3)
            # print('Mixing the ingredients...')
            # time.sleep(3)
            # print('Making the coffee...')
            # time.sleep(3)

            if money >= drink["cost"]:
                print(f'Here is your {coffee_prompt}. Enjoy! ☕')
                profit += money

            else:
                print("Sorry that's not enough money. Money refunded.")