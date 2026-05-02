Menu = {
    "latte" : {
        "ingredients" : {
            "water" : 150,
            "milk" : 80,
            "coffee" : 21,
        },
        "cost" : 128
    },
    "expresso" : {
        "ingredients" : {
            "water" : 150,
            "coffee" : 30,
        },
        "cost" : 220
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 800,
            "milk" : 100,
            "coffee" : 20,
        },
        "cost" : 350
    }
}

resources = {
    "water" : 500,
    "milk" : 900,
    "coffee" : 500,
 }

profit = 0

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, you don't have enough resources to buy this coffee {item}")
            return False
        return True
def make_money():
    print("Please insert coins: ")
    total =0
    coins_five = int(input("Please insert 5rs coins: "))
    coins_ten = int(input("Please insert 10rs coins: "))
    coins_twenty = int(input("Please insert 20rs coins: "))
    total = total + coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        balance = money_received - coffee_cost
        print(f"Here is your balance: Rs:{balance}")
        return True
    else:
        print("Sorry, you don't have enough resources to pay this coffee")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your coffee: {coffee_name}☕ Enjoy...")

is_on = True
while is_on:
    print("Welcome to the coffee machine!☕🍵")
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs:{profit}")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = make_money()
            if payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])