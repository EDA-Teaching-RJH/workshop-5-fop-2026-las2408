#Inputs
def money():
    total_due = 75
    coins = ["5","10","20","50"]

    while total_due > 0:
         print(f"Amount due: {total_due}")
         coin = input("Insert coin: ")
         if coin in coins:
             total_due -= int(coin)
         else:
            print("Invalid Coin")

    if total_due < 0:
        print(f"Amount owed: {total_due * -1}")

    else:
        print(f"Total balance = 0")

money()