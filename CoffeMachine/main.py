from menu import MENU


def total_money(check_bill):
    global now_money
    now_money += check_bill


def check_transaction(name_drink):
    # TODO: 3.Process coins.
    print("Please insert coins.")
    coin = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    each_coin = []
    for name in coin:
        each_coin.append(int(input(f"how many {name} : ")) * coin[name])

    total_clash = sum(each_coin)
    cal_price = MENU[name_drink]['cost']

    # TODO: 4.Check transaction successful?
    if total_clash > cal_price:
        total_money(cal_price)
        make_coffee(name_drink)
        change = total_clash - cal_price
        print(f"Here is ${change:0.2f} dollars in change.")
        print(f"Here is your{name_drink} ☕.Enjoy!")
    elif total_clash < cal_price:
        print("Sorry that's not enough money. Money refunded.")
        machine()
    else:
        total_money(cal_price)
        make_coffee(name_drink)
        print(f"Here is your {name_drink} ☕.Enjoy!")


def check_stock(name_drink):
    # TODO: 2.Check resources sufficient to make drink order.
    check_bill = False
    for item in MENU[name_drink]['ingredients']:
        if resources[item] < MENU[name_drink]['ingredients'][item]:
            print(f"Sorry there is not enough {item}")
            check_bill = False
            break
        else:
            check_bill = True

    if check_bill:
        check_transaction(name_drink)
    else:
        machine()


def make_coffee(name_drink):
    # TODO: 5.Make Coffee.
    for item in MENU[name_drink]['ingredients']:
        resources[item] -= MENU[name_drink]['ingredients'][item]


def machine():
    while not out_of_stock and not turn_on_machine:
        # TODO: 1.Prompt user by asking "What would you like?".
        customer_pick = input("What would you link? (espresso / latte / cappuccino) : ").lower()
        if customer_pick == "report":
            print(f"{[*resources][0]} : {resources['water']} ml.")
            print(f"{[*resources][1]} : {resources['milk']} ml.")
            print(f"{[*resources][2]} : {resources['coffee']} g.")
            print(f"Money: ${now_money}")
        elif customer_pick not in MENU:
            print("You wrong type,please type again")
            machine()
        else:
            check_stock(customer_pick)


turn_on_machine = False
out_of_stock = False
now_money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine()
