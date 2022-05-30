def report(machine_resources):
    """
    That function prints the resources remaining on the machine
    :param machine_resources: that is the resources of the machine, reference to global resources
    """
    for key, value in machine_resources.items():
        print(f'{key.capitalize()}: ', end='')
        if key == 'coffee':
            print(f'{value}g')
        elif key == 'money':
            print(f'${value}')
        else:
            print(f'{value}ml')


def is_resources_enough(machine_resources, choice):
    """
    That function check if there are enough ingredients on the machine before make the recipe
    :param machine_resources: that is the resources of the machine, reference to global resources.
    :param choice: that is the drink choosen by the user, used to access the ingredients of the recipe.
    :return: True if the amount of the ingredients in the machine are enough for the recipe, False if not and prints
    the missing ingredient.
    """
    from data import MENU
    ingredients = MENU[choice]['ingredients']
    for key, value in ingredients.items():
        if value > machine_resources[key]:
            print(f'There is not enough {key}')
            return False
    return True


def process_coins():
    """
    That function checks the amount of any kind of coin and adds the total value to a variable
    :return: the total amount of money
    """
    total = 0
    coins = {'quarter': 0.25, 'dime': 0.10, 'nickel': 0.05, 'penny': 0.01 }
    for key, value in coins.items():
        total += int(input(f'How many {key}?: ')) * value
    return total


def check_transaction(choice, total):
    """
    That function check if the payinment is enough to get the coffee
    :param choice: the choice of the user to find the cost of it.
    :param total: the amount of money given by the user
    :return: refund that is the change of user and cash that is the price of the drink
    """
    from data import MENU
    if MENU[choice]['cost'] > total:
        return total, 0
    else:
        refund = total - MENU[choice]['cost']
        cash = MENU[choice]['cost']
        return refund, cash


def make_coffee(machine_resources, choice):
    """
    That function subtracts the ingredients of resources to make the coffee
    :param machine_resources: reference to the global resources variable
    :param choice: the drink choosen
    :return: Nothing
    """
    from data import MENU
    ingredients = MENU[choice]['ingredients']
    for key, value in ingredients.items():
        machine_resources[key] -= value


def main():
    """
    That is a recursive function that calls the other functions to make the drink.
    :return:
    """
    global resources
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose == 'off':
        return
    if choose == 'report':
        report(resources)
    else:
        total = process_coins()
        refund, cash = check_transaction(choose, total)
        if cash == 0:
            print(f'Sorry, that\'s not enough money. {refund} refunded.')
        else:
            if is_resources_enough(resources, choose):
                resources['money'] += cash
                make_coffee(resources, choose)
                print(f'Here is ${refund:.2f} in change.')
                print(f'Here is your {choose}')
            else:
                print(f'Here is your ${total} back.')
    main()


resources = {'water': 300, 'milk': 200, 'coffee': 100, 'money': 0}
main()
