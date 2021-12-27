from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    # TODO: 1.Prompt user by asking "What would you like?"
    option = menu.get_items()
    choice = input(f"What would you like? ({option}) : ").lower()

    # TODO: 2.Turn off the coffee by entering "off" to the prompt.
    if choice == 'off':
        is_on = False

    # TODO: 3.Print report.
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice not in option:
        print("Wrong type!")
    else:
        drink = menu.find_drink(choice)

        # TODO: 4.Check resources sufficient.
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)

        # TODO: 5.Process coins.
        # TODO: 6.Check transaction successful.
        is_payment_successful = money_machine.make_payment(drink.cost)

        if is_enough_ingredients and is_payment_successful:
            # TODO: 7.Make coffee.
            coffee_maker.make_coffee(drink)
