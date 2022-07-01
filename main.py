from coffee_machine_resources import MENU, resources


def report():
    print(f'Water: {resources["water"]}ml\n'
          f'Milk: {resources["milk"]}ml\n'
          f'Coffee: {resources["coffee"]}g\n'
          f'Money: ${"{:.2f}".format(resources["money"])}')


def drink_maker(drink_type):
    drink = MENU[drink_type]

    if resources_sufficient(drink) and payment_processor(drink_type):
        for ingredient in drink["ingredients"]:
            resources[ingredient] -= drink["ingredients"][ingredient]


def resources_sufficient(drink):
    can_make = True
    for ingredient in drink["ingredients"]:
        if drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            can_make = False

    return can_make


def coin_getter():
    quarters = 0.25 * int(input("How many quarters?: "))
    dimes = 0.1 * int(input("How many dimes?: "))
    nickels = 0.05 * int(input("How many nickels?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    return quarters + dimes + nickels + pennies


def payment_processor(drink_type):
    drink = MENU[drink_type]
    cost = drink["cost"]
    print(f"That will be ${'{:.2f}'.format(cost)}. Please insert coins.")
    payment = coin_getter()

    if payment >= cost:
        print(f"Here is ${'{:.2f}'.format(payment - cost)} in change.")
        resources["money"] += drink["cost"]
        print(f"Here is your {drink_type} ☕ Enjoy!")
        paid = True
    else:
        print("Sorry that's not enough money. Money refunded.")
        paid = False

    return paid


user_choice = "on"
while user_choice != "off":
    # Prompt user: "espresso", "latte", or "cappuccino" (secret options: "off" or "report" for maintainers of the
    # coffee machine)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report()
    elif user_choice != "off":
        drink_maker(user_choice)
