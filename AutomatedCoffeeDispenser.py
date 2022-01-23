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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
bank = 5.00
power = 'off'
QUART, DIME, NICK, PENN = 0.25, 0.10, 0.05, 0.01


def check():
    return [resources['water'], resources['milk'], resources['coffee']]


def report():
    print(f'''The coffee dispenser contains {resources['water']}ml of water,{resources['milk']}ml of milk,
{resources['coffee']}g of coffee with a balance of ${bank} in change''')


def pow():
    global power
    power = input("Would you like to (on/off) the system?").lower()


def refill():
    report()
    wa = int(input("How much water would you like to fill: "))
    mk = int(input("How much milk would you like to add: "))
    cf = int(input("How much coffee would you like to add: "))
    resources['water'] += wa
    resources['milk'] += mk
    resources['coffee'] += cf
    print(report())


var = True
while var:
    print('######### COFFEE MACHINE#########\n'
          '1)Power(1)\n'
          '2)Print Report(2)\n'
          '3)Add resources')
    q = int(input())
    if q == 1:
        pow()
    elif q == 2:
        report()
    elif q == 3:
        refill()
    while power == 'on':
        ch = input("What would you like to drink(espresso/latte/cappuccino)\n").lower()
        w, m, c = MENU[ch]['ingredients']['water'], MENU[ch]['ingredients']['milk'], MENU[ch]['ingredients']['coffee']
        ing, ing1, cont = [w, m, c], ['water', 'milk', 'coffee'], "y"
        res = check()
        for i in range(0, 3):
            if res[i] >= ing[i]:
                print(f"Sufficient {ing1[i]} exists....")
                resources[ing1[i]] -= ing[i]
            else:
                print("Sufficient {ing1[i]} doesn't exists. Please try again later")
                cont = "n"
                break
        if cont != "y":
            print("Sorry the problem will be sorted ASAP")
            break
        print(f"While the coffee is being made please provide ${MENU[ch]['cost']} for your {ch}")
        q = int(input("How many quarters?")) * QUART
        n = int(input("How many nickels?")) * NICK
        d = int(input("How many dimes?")) * DIME
        p = int(input("How many pennies?")) * PENN
        net = q + n + d + p
        balance = round(net - MENU[ch]['cost'], 2)
        if balance > 0:
            print(f"Please collect ${balance} as your balance")
            bank += MENU[ch]['cost']
            print("Please collect your drink")
        elif balance < 0:
            print("Sorry insufficient funds provided")
            break
        else:
            print("Thanks for tendering exact change")
            print("Please collect your drink")

        print("Thanking for using our system. Going to hibernate until further actions")
        pow()
    var = not (input('Break the machine?(True/False)')).capitalize()
