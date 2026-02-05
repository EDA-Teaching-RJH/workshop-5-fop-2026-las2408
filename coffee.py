#Statement of Requirements
#Inputs accpeted are 5,10,20,50, any other coins are considered invalid and programme stops
#If a string is entered rather than a integer, the programme will crash
def money():
    total_due = 75
    coins = ["5","10","20","50"]

    def get_coin():
        while total_due > 0:
            print(f"Amount due: {total_due}")
            coin = input("Insert coin: ")

    def update_total(coin):
            if coin in coins:
                total_due -= int(coin)
            else:
                print("Invalid Coin - Please try again")
                

    if total_due < 0:
        print(f"Amount owed: {total_due * -1}")

    else:
        print(f"Total balance = 0")

def get_coin():
    """Handles INPUT: Prompts the user and ensures the coin is valid."""
    accepted_coins = [5, 10, 20, 50]
    while True:
        try:
            coin = int(input("Insert coin (5, 10, 20, 50): "))
            if coin in accepted_coins:
                return coin
            else:
                print("Invalid coin. We only accept 5, 10, 20, or 50.")
        except ValueError:
            print("Please enter a number.")

def update_total(current_due, coin):
    """Handles CALCULATION: Subtracts the coin from the amount owed."""
    return current_due - coin

def dispense_product(final_balance):
    """Handles OUTPUT: Calculates change and finishes the transaction."""
    # If final_balance is negative, that's the change owed to the user
    change = abs(final_balance)
    print("---")
    print(f"Enjoy your coffee! Your change is: {change}")

def main():
    amount_due = 75
    
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        # 1. Get Input
        coin = get_coin()
        # 2. Calculate
        amount_due = update_total(amount_due, coin)
    
    # 3. Output
    dispense_product(amount_due)

if __name__ == "__main__":
    main()