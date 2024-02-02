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
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
            order_ingredients[item] >= resources[item]
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    total = int(input("how many quarters?: ")) * 0.025
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

is_on = True

while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice == "off":
         is_on = False
    elif choice == "report":
         print(f"Water: resources['water']")
         print(f"Milk: resources['milk']ml")
         print(f"Coffee: resources['coffee'] g")
         print(f"Money: ${profit}")
              
    else:
         drink = MENU[choice]      
         is_resources_sufficient(drink["ingredients"])    