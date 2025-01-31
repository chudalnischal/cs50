def main ():
    coins = [25, 10, 5]
    amountDue = 50
    checking(coins, amountDue)


def checking(coins,amountDue):
    while amountDue > 0:
        userInput = int(input("Insert Coins: "))
        if userInput in coins:
            amountDue = amountDue - userInput
            if amountDue == 0:
               chargedOwned = 0
               print("Change Owed:",chargedOwned)
            elif amountDue < 0:
                chargedOwned = amountDue * -1
                print("Change Owed:",chargedOwned)
            else:
                print("Amount Due:", amountDue)
        else:
            print("Amount Due:", amountDue)

main()
