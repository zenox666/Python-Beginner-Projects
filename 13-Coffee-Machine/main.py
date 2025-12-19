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



def resources_sufficient(item):
    is_enough = True
    for i in item:
        if item[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            is_enough =  False
            return is_enough
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(needed, given):
    if given >= needed:
        change = round(given - needed, 2)
        print(f"Here is ${change} in change.")
        global money
        money += needed
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(order_ingredients,drink_name):

    for i in order_ingredients:
        resources[i] = resources[i] - order_ingredients[i]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


money = 0
is_on = True

while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino) or 'report' or off:")

    if choice=='off':
        is_on = False

    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {money}$")

    elif choice in MENU:
        drink = MENU[choice]
        if resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(drink['cost'],payment):
                make_coffee(drink['ingredients'],choice)
    else:
        print("Invalid choice. Please try again.")
