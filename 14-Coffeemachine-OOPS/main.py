from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    items = menu.get_items()
    choice = input(f"What would you like? {items} or 'report' or off:")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        resources_sufficient = coffe_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)
        if resources_sufficient and payment:
            coffe_maker.make_coffee(drink)
