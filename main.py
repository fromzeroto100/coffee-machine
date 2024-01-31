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



recources = {
    "water": 300,
    "milk": 250,
    "coffee": 100

}

def is_recources_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > recources[item]:
            print(f"Sorry there is not enought {item}.")
            return False
    return True

def process_coins():
    print("Insert your coins.") 
    total = int(input("How many quarters")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enought money. Money refunded")
        return False




    


input("What would like to drink? (espresso/latte/ cappuccino)")

