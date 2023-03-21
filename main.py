from Menu import MENU
from Menu import resources


def verificare(coffe):
    if MENU[coffe]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return 0
    elif MENU[coffe]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return 0
    elif MENU[coffe]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return 0
    else:

        print(f"It will cost ${MENU[coffe]['cost']}")
        return 1


resources['money'] = 0
Machine = True
while Machine:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "off":
        Machine = False
        print("Machine is turning off")
    elif order == "report":
        for p in resources:
            print(f"{p}: {resources[p]}")
    else:
        x = verificare(order)
        if x != 0:
            quarters = int(input("Insert quarters:")) * .25
            dimes = int(input("Insert dimes:")) * .1
            nickles = int(input("Insert nickles:")) * .05
            pennies = int(input("Insert pennies:")) * .01
            money = quarters + dimes + nickles + pennies
            if money < MENU[order]['cost']:
                print('''Sorry that's not enough money. Money refunded.''')
            else:
                change = money - MENU[order]['cost']
                resources['money'] += MENU[order]['cost']
                if change != 0:
                    print(f'''Here is youre change: ${round(change * 100) / 100}''')
                print(f'''Here is youre {order}''')
                for p in MENU[order]['ingredients']:
                    resources[p] = resources[p] - MENU[order]["ingredients"][p]

