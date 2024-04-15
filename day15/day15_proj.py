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

total = [0]
coins = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

report = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    print(f"Water: {report['water']}ml")
    print(f"Milk: {report['milk']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${total[0]}")

def check_resources(prompt_user):
    for value in MENU[prompt_user]['ingredients']:
        if report[value] - MENU[prompt_user]['ingredients'][value] <= 0:
            print(f"Sorry there is not enough {value}.")
            return False
    return True

def insert_coins(drink, total):
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total[0] += coins["quarter"] * quarters + coins["dime"] * dimes + coins["nickel"] * nickles + coins["penny"] * pennies

    if total[0] < MENU[drink]["cost"]:
        total[0] -= coins["quarter"] * quarters + coins["dime"] * dimes + coins["nickel"] * nickles + coins["penny"] * pennies
        return print("Sorry that's not enough money. Money refunded.")
    else:
        return user_drink(drink)

def give_change(drink):
    total[0] -= MENU[drink]["cost"]
    total[0] = round(total[0], 2)
    print(f"Here is ${total[0]} in change.")
    print(f"Here is your {drink}. Enjoy!")
    
def user_drink(drink):
    for value in MENU[drink]["ingredients"]:
        report[value] -= MENU[prompt_user]['ingredients'][value]
    give_change(drink)

prompt_user = ""
while prompt_user != "off":
    prompt_user = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt_user == "report":
        print_report()
    elif prompt_user == "off":
        break
    else:
        if check_resources(prompt_user):
            insert_coins(prompt_user, total)





    