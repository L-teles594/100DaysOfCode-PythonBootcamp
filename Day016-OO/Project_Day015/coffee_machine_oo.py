from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    # Prompt asking
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    # Turn off the machine by the prompt
    if choice == 'off':
        return
    # Print report by the prompt
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
        main()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        # Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Process coins/Check transaction successful/Make coffee
            coffee_maker.make_coffee(drink)
        main()


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
main()
