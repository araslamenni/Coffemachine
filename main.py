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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resources_sufficient(resources, order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("please insert coin!")
    total = int(input(f"How many quarters?: ")) * 0.25
    total += int(input(f"How many dimes?: ")) * 0.10
    total += int(input(f"How many nickles?: ")) * 0.05
    total += int(input(f"How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} is change")
        global profit
        profit += drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(name_drink, order_ingredients):
    for item in order_ingredients:
        resources[item] - order_ingredients[item]
    print(f"Here is you {drink}. Enjoy.")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $ {profit}")
        
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coin()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

