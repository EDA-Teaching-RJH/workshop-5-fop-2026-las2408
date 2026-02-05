#Statement of Requirements
#Inputs accpeted are 5,10,20,50, any other coins are considered invalid and programme stops
#If a string is entered rather than a integer, the programme will crash
def money():
    total_due = 75
    coins = ["5","10","20","50"]

    while total_due > 0:
         print(f"Amount due: {total_due}")
         coin = input("Insert coin: ")
         if coin in coins:
             total_due -= int(coin)
         else:
            print("Invalid Coin - Please try again")
            continue

    if total_due < 0:
        print(f"Amount owed: {total_due * -1}")

    else:
        print(f"Total balance = 0")

money()