import json
import random

def set_prices():
    with open("default_coins.txt") as coins_file:
        coins = json.loads(coins_file.read())
        with open("settings.txt", "w") as file:
            for i in range(100):
                unreal_coins = [*coins]
                plus_10 = []
                minus_10 = []
                plus_30 = []
                minus_30 = []
                massive_2 = []
                for i in range(6):
                    coin = random.choice(unreal_coins)
                    plus_10.append(coin)
                    unreal_coins.remove(coin)
                for i in range(6):
                    coin = random.choice(unreal_coins)
                    minus_10.append(coin)
                    unreal_coins.remove(coin)
                for i in range(3):
                    coin = random.choice(unreal_coins)
                    plus_30.append(coin)
                    unreal_coins.remove(coin)
                for i in range(3):
                    coin = random.choice(unreal_coins)
                    minus_30.append(coin)
                    unreal_coins.remove(coin)
                for i in range(2):
                    coin = random.choice(unreal_coins)
                    massive_2.append(coin)
                    unreal_coins.remove(coin)
                for c in coins:
                    if c in plus_10:
                        c["value"] = c["value"] * random.choice([1.1, 1.15, 1.2])
                    elif c in minus_10:
                        c["value"] = c["value"] * random.choice([0.9, 0.95, 0.8, 0.85, 0.75])
                        if c["value"] < 0.1:
                            c["value"] = 0.1
                    elif c in plus_30:
                        c["value"] = c["value"] * random.choice([1.3, 1.35, 1.4])
                    elif c in minus_30:
                        c["value"] = c["value"] * random.choice([0.7, 0.65, 0.6])
                        if c["value"] < 0.1:
                            c["value"] = 0.1
                    elif c in massive_2:
                        c["value"] = c["value"] * random.choice([1.6, 0.4])
                        if c["value"] < 0.1:
                            c["value"] = 0.1
                    c["value"] = float(f"{c['value']:.2f}")
                file.write(json.dumps(coins))
                file.write("\n")

