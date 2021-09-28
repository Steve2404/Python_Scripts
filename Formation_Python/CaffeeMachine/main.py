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
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(oder_ingredient):
    for item in oder_ingredient:
        if oder_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return  False
    return True
def process_coin():
    print("Please insert coins.")
    total = int(input("How many quarters ?: "))*0.25
    total += int(input("How many dimes ?: "))*0.1
    total += int(input("How many nickles ?: "))*0.05
    total += int(input("How many pennies ?: "))*0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change}  change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

is_finished = False

while not is_finished:
    #"TODO: Prompt user by asking"
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_finished = True
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            is_transaction_successful(payment, drink["cost"])