MENU = {
    "espresso": {
        "ingredients": {
            "water": 150,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 21,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 200,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 900,
    "milk": 700,
    "coffee": 100,
    "money": 0
}


###### Step-3 : Function to reduce Quantity After Serving Every Cup of Cofee.....
def resource_reducer(coffee_name,resources):
    resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_name]["cost"]


###### Step-2 : Function to Get Coin and Validate amount and Serve Cofee.....
def amount_checker(coffee_n):
    print("Enter Coins")
    no_quarter = int(input("How many quarters? : "))
    no_dime = int(input("How many dimes? : "))
    no_nickle = int(input("How many nickles? : "))
    no_pennie = int(input("How many pennies? : "))
    total_coin_value = (no_quarter * 0.25) + (no_dime * 0.10) + (no_nickle * 0.05) + (no_pennie * 0.01)
    if total_coin_value > MENU[coffee_n]["cost"]:
        print(f"Here is ${total_coin_value - MENU[coffee_n]["cost"] : .2f} in change")
        resource_reducer(coffee_n,resources)
        print(f"Here is Your {coffee_n} ☕ enjoy\n")
        coffee_machine()
    elif total_coin_value < MENU[coffee_n]["cost"]:
        print("Sorry that's not enough Money...     Money refunded....\n")
        coffee_machine()
    else:
        print(f"Here is Your {coffee_n} ☕ enjoy\n")
        resource_reducer(coffee_n,resources)
        coffee_machine()

######  Step-1 : Function to Check Reqirements of Coffee Ordered Before Making
def coffee_requirement(coffee_name, resources):
    requirements = True
    insufficient_resources = []
    for ingredient, amount in MENU[coffee_name]["ingredients"].items():
        if resources[ingredient] < amount:
            insufficient_resources.append(ingredient)
            requirements = False
            
    if requirements:
        amount_checker(coffee_name)
    else:
        for resource in insufficient_resources:
            print(f"There is less {resource} in the Coffee Machine")

######  Main Function
def coffee_machine():
    coffee_type = input("What would you like? \nEnter 'e' for espresso \nEnter 'l' for latte \nEnter 'c' for cappuccino \nEnter 'r' to Print Reamining Raw Material  : ")
    if coffee_type == 'e':
        coffee_n = "espresso"
        coffee_requirement(coffee_n,resources)
    elif coffee_type == 'l':
        coffee_n = "latte"
        coffee_requirement(coffee_n,resources)
    elif coffee_type == 'c':
        coffee_n = "cappuccino"
        coffee_requirement(coffee_n,resources)
    elif coffee_type == 'r':
        print(f"Water = {resources["water"]}ml")
        print(f"Milk = {resources["milk"]}ml")
        print(f"Coffee = {resources["coffee"]}g")
        print(f"Money = ${resources["money"] : .2f}\n")
        coffee_machine()


coffee_machine()


