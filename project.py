from termcolor import colored
from tabulate import tabulate

import os
import time
import sys
import json

import settings


status = 1
inner_status = 0
name = ""
coins = {}
previous_coins = {}
wallet = {}
days = 0
cash = 0

def main():
    global status, inner_status, previous_coins
    while status:
        match main_menu():
            case 1:
                os.system("clear")
                print_header("PYVESTOR")

                is_new = input("(1) Resume\n(2) New Game\n\n: ")
                if is_new == "1":

                    if set_settings():
                        pass
                    else:
                        os.system("clear")
                        print(colored("\n\n\n(No saved data found.)\n\n\n", "red"))
                        time.sleep(1.5)
                        continue

                elif is_new == "2":

                    if fac_settings():
                        pass
                    else:
                        sys.exit("An error detected.")

                else:
                    invalid_selection()
                    continue

                inner_status = 1
                waiting(1)
                while inner_status:
                    match game_menu():
                        case 1:
                            if get_coins():
                                successfully_done()
                            else:
                                pass
                        case 2:
                            while not get_wallet():
                                pass
                        case 3:
                            if waiting():
                                pass
                            else:
                                sys.exit("An error detected.")
                        case 4:
                            if save_game():
                                break
                        case _:
                            invalid_selection()
            case 2:
                help()
            case 3:
                print(colored("You successfully quitted.", "red"))
                status = 0
            case _:
                invalid_selection()


def main_menu(selection=None):
    if selection == None:
        os.system("clear")
        print_header("PYVESTOR")
        selection = input(f"""{f'{colored("(1) Play", "green")}'}\n{f'{colored("(2) Help", "yellow")}'}\n{f'{colored("(3) Quit", "red")}'}\n\n: """)
    if selection not in ["1", "2", "3"]:
        return False
    else:
        return int(selection)


def invalid_selection():
    os.system("clear")
    print(colored("\n\n\n(Make a valid selection!)\n\n\n", "yellow"))
    time.sleep(1)

def successfully_done():
    os.system("clear")
    print(colored("\n\n\n(Your transaction is successfully done!)\n\n\n", "green"))
    time.sleep(2)



def game_menu(selection=None):
    if selection == None:
        os.system("clear")
        print_header("PYVESTOR")
        selection = input(f"""(1) Market\n(2) Wallet\n(3) Wait\n{f'{colored("(4) Save & Quit", "yellow")}'}\n\n: """)
    if selection not in ["1", "2", "3", "4"]:
        return False
    else:
        return int(selection)


def fac_settings():
    global name, wallet, coins, days, cash

    # defining the user's name
    while True:
        name = input("\nWhat is your investor name? ").strip()
        if not name:
            print("Enter a valid name.")
            continue
        else:
            break

    # taking coins list
    with open("default_coins.txt") as def_coins_file:
        coins = json.loads(def_coins_file.read())
        with open("coins.txt", "w") as coins_file:
            coins_file.write(def_coins_file.read())

    # cleaning saved.txt
    with open("saved.txt", "w") as saved_file:
        saved_file.write("")

    # setting the wallet
    wallet = {}
    for c in coins:
        wallet[f"{c['shorten']}"] = 0

    days = 0
    cash = 100

    settings.set_prices()
    return True



def set_settings():
    global name, wallet, coins, days, cash, previous_coins
    with open("coins.txt") as coins_file:
        str_coins_file = coins_file.read()
        if not str_coins_file:
            return False
        coins = json.loads(str_coins_file)
    with open("saved.txt") as saved_file:
        str_saved = saved_file.read()
        if not str_saved:
            return False
        saved = json.loads(str_saved)
        name = saved["name"]
        days = saved["days"]
        wallet = saved["wallet"]
        cash = saved["cash"]
        previous_coins = saved["previous"]
    return True


def save_game():
    global status, inner_status, name, coins, wallet, days, cash
    try:
        with open("coins.txt", "w") as coins_file:
            coins_file.write(json.dumps(coins))
        with open("saved.txt", "w") as saved_file:
            saved = {"name": name, "days": days, "wallet": wallet, "cash": cash, "previous": previous_coins}
            saved_file.write(json.dumps(saved))
        status = 1
        inner_status = 0
        name = ""
        coins = {}
        wallet = {}
        days = 0
        cash = 0
        os.system("clear")
        print(colored("\n\n\n(Your game is successfully saved!)\n\n\n", "green"))
        time.sleep(1)
        return True
    except:
        return False


def help():
    os.system("clear")
    print_header("HELP")
    print(colored("How to start?", "cyan"), "\n    Type '1' to play. You will be prompted 'New game/Resume', make your selection; you will be sent to the game screen.")
    print(colored("\nHow to play?", "cyan"), "\n    You have 4 options:\n        (1) Market - It prompts you a list of coins in the market and you will have the right to buy or sell coins based on your assets.")
    print("        (2) Wallet - It prompts you your wallet with your current coins and cash balance.")
    print("        (3) Wait - It allows you to wait as many days as you want, to see how the market goes.")
    print("        (4) Save & Quit - It allows you to return back to main menu, when you select this, your data is automatically saved.")
    print(colored("\nHave fun!\n\n", "magenta"))
    input("(Press Enter to go back)")


def get_wallet():
    os.system("clear")
    print_header("WALLET")
    header = ["Coin", "Value", "Yours", "Worth ($)"]
    table = []
    counter = 1
    for coin in wallet:
        if wallet[coin] > 0:
            r_coin = [c for c in coins if c["shorten"] == coin][0]
            table.append([f"({counter}) {r_coin['name']} ({r_coin['shorten']})", f"${r_coin['value']}", f"{wallet[coin]}", f"${float(wallet[coin] * r_coin['value']):.2f}"])
            counter += 1
    print(tabulate(table, headers=header, tablefmt="github"))
    print(colored("\n(Type 0 to go back)", "yellow"))
    while True:
        try:
            selection = int(input("\nCoin Number: "))
            if selection == 0:
                return True
            if 0 < selection <= len(table):
                os.system("clear")
                print_header("COIN")
                coin_name = table[selection-1][0].split("(")[-1].split(")")[0]
                coin = [c for c in coins if c["shorten"] == coin_name][0]
                in_header = ["Coin", "Value", "Yours", "Worth ($)"]
                in_table = [[f"{coin['name']} ({coin['shorten']})", f"${coin['value']}", f"{wallet[coin['shorten']]}", f"${float(wallet[coin['shorten']] * coin['value']):.2f}"]]
                in_done_table = tabulate(in_table, headers=in_header, tablefmt="grid")
                print(in_done_table)
                in_or_di = input(f"""\n{f'{colored("(1) Invest", "green")}'}\n{f'{colored("(2) Divest", "red")}'}\n(3) Go back\n\n: """)
                if in_or_di in ["1", "2", "3"]:
                    if in_or_di == "1":
                        if invest(coin, in_done_table):
                            successfully_done()
                            return True
                        else:
                            return False
                    elif in_or_di == "2":
                        if divest(coin, in_done_table):
                            successfully_done()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    invalid_selection()
                    return False
            else:
                invalid_selection()
                return False
        except ValueError:
            invalid_selection()
            return False




def print_header(head):
    if name:
        header = (colored(f"{head}                      Name: {name} | Cash: ${cash:,} | Days: {days}", "green"))
        print(header)
        print(colored("-"*(len(header)-5), "green"), end="\n\n")
    else:
        print(colored(f"{head}                      Author: Muhammed B. Anbarpinar | Language Used: Python | Project Name: PYVESTOR", "green"))
        print(colored("---------------------------------------------------------------------------------------------------------------\n", "green"))

def get_coins():
    while True:
        os.system("clear")
        print_header("MARKET")
        print()
        coins_table = [[f"({coins.index(coin) + 1}) {coin['name']} ({coin['shorten']})", f"${coin['value']}"] for coin in coins]
        if len(previous_coins) == 20:
            for i in range(20):
                if coins[i]["value"] < previous_coins[i]["value"]:
                    down_arrow = "\u2193"
                    coins_table[i][-1] = f"""{coins_table[i][-1]} {f'{colored(down_arrow, "red")}'}"""
                elif coins[i]["value"] > previous_coins[i]["value"]:
                    up_arrow = "\u2191"
                    coins_table[i][-1] = f"""{coins_table[i][-1]} {f'{colored(up_arrow, "green")}'}"""
        header = ["Coin", "Value"]
        print(tabulate(coins_table, headers=header, tablefmt="github"))
        print(colored("\n(Type 0 to leave)", "yellow"))
        try:
            selection = int(input("\nCoin Number: "))
            if selection == 0:
                return 0
            elif 1 <= selection <= 20:
                while True:
                    os.system("clear")
                    print_header("COIN")
                    coin = coins[selection-1]
                    in_header = ["Coin", "Value", "Yours", "Worth ($)"]
                    in_table = [[f"{coin['name']} ({coin['shorten']})", f"${coin['value']}", f"{wallet[coin['shorten']]}", f"${(wallet[coin['shorten']] * coin['value']):.2f}"]]
                    in_done_table = tabulate(in_table, headers=in_header, tablefmt="grid")
                    print(in_done_table)
                    in_or_di = input(f"""\n{f'{colored("(1) Invest", "green")}'}\n{f'{colored("(2) Divest", "red")}'}\n(3) Go back\n\n: """)
                    if in_or_di in ["1", "2", "3"]:
                        if in_or_di == "1":
                            if invest(coin, in_done_table):
                                return True
                            else:
                                pass
                        elif in_or_di == "2":
                            if divest(coin, in_done_table):
                                return True
                            else:
                                pass
                        elif in_or_di == "3":
                            break
                    else:
                        invalid_selection()
            else:
                invalid_selection()
        except ValueError:
            invalid_selection()


def invest(c, t):
    global wallet, cash
    try:
        os.system("clear")
        print_header("INVEST")
        print(t)
        amount = int(input(f"""\nHow many do you want to buy ({f'{colored("0 to cancel", "yellow")}'})?\n\n: """))
        if amount == 0:
            return False
    except ValueError:
        invalid_selection()
        return False

    total = round(float(amount * c["value"]), 2)
    if total <= cash:
        cash = round(float(cash - total), 2)
        wallet[c["shorten"]] += amount
        return True
    else:
        os.system("clear")
        print(colored("\n\n\n(Not enough cash!)\n\n\n", "red"))
        time.sleep(1)
        return False




def divest(c, t):
    global wallet, cash
    try:
        os.system("clear")
        print_header("DIVEST")
        print(t)
        amount = int(input(f"""\nHow many do you want to sell ({f'{colored("0 to cancel", "yellow")}'})?\n\n: """))
        if amount == 0:
            return False
    except ValueError:
        invalid_selection()
        return False

    if amount <= wallet[c["shorten"]]:
        wallet[c["shorten"]] -= amount
        cash = round(cash + (amount * c["value"]), 2)
        return True
    else:
        os.system("clear")
        print(colored("\n\n\n(Not enough coins!)\n\n\n", "red"))
        time.sleep(1)
        return False


def waiting(override=None):
    global coins, days, previous_coins
    while True:
        try:
            if days != 0:
                if override == None:
                    day_number = int(input(f"""\nHow many days do you want to wait ({f'{colored("0 to cancel", "yellow")}'})? """))
                else:
                    return None
            else:
                day_number = 1
            if 0 < day_number:
                previous_coins = coins
                for i in range(day_number):
                    if days <= 99:
                        with open("settings.txt") as file:
                            daily_coins = json.loads(file.readlines()[days-1])
                            coins = daily_coins
                        days += 1
                    else:
                        finish_game()
                return True
            if 0 == day_number:
                return True
            else:
                continue
        except ValueError:
            print(colored("Invalid selection!", "red"))
            continue


def finish_game():
    global cash
    try:
        for c in wallet:
            if wallet[c] > 0:
                for coin in coins:
                    if coin["shorten"] == c:
                        cash = cash + float(f"{(coin['value'] * wallet[c]):.2f}")
    except:
        input("hata")
    os.system("clear")
    print_header("END")
    if cash > 50000:
        print(colored(f"You are an extraordinary investor! You started with $100 and now you have ${cash}. Bravo!", "green"))
    elif cash > 25000:
        print(colored(f"You are a great investor! You started with $100 and now you have ${cash}. Bravo!", "green"))
    elif cash > 10000:
        print(colored(f"You are a very good investor! You started with $100 and now you have ${cash}. Bravo!", "blue"))
    elif cash > 5000:
        print(colored(f"You are an okay investor. You started with $100 and now you have ${cash}. Enjoy!", "blue"))
    elif cash > 1000:
        print(f"You are not a great investor. But you are at least survived. You started with $100 and now you have ${cash}. Bye!")
    elif cash > 100:
        print(colored(f"You better stay out of the market! You started with $100 and now you have only ${cash}. Learn better!", "red"))
    else:
        print(colored(f"You a terrible investor! You started with $100 and now you have only ${cash}. Loser!", "red"))

    with open("coins.txt", "w") as coins_file:
        coins_file.write("")
    with open("saved.txt", "w") as coins_file:
        coins_file.write("")


    input("\n\nCongrats! You successfully (or unsuccessfully, whatever) finished the game! \nYou can start again by using new game feature to improve yourself in investment.\n\n(Press enter to close the game)")
    sys.exit("---")

if __name__ == "__main__":
    main()
