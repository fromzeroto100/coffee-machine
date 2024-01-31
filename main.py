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

    

    


input("What would like to drink? (espresso/latte/ cappuccino)")

