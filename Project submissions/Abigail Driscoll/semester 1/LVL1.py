balance = 1000

Wlist = []
Dlist = []

# Empty list to store withdraw and deposit amounts for each session

bank = True
def bank_account():
    choice = input("Would you like to deposit(D), withdraw(W), view balance(B), see transactions(T) or exit(E): ")

    if choice.upper() == "W":
        withdrawal = int(input("How much would you like to withdraw? (£): "))
        if balance - withdrawal < 0:
            print("Transaction not possible. You have insufficient funds")
        else:
            print("Your new balance is: ", balance - withdrawal)
            Wlist.append(withdrawal)
            bank = True

    if choice.upper() == "D":
        deposit = int(input("How much would you like to deposit? (£): "))
        print("Your new balance is: ", balance + deposit)
        Dlist.append(deposit)
        bank = True

    if choice.upper() == "B":
        print(balance)
        bank = True

    if choice.upper() == "T":
        for i in Wlist:
            print ("Withdrawal: ", i)
        for i in Dlist:
            print ("Deposit: ", i)
        bank = True

    if choice.upper() == "E":
        raise SystemExit("Goodbye")
        bank = False

while bank == True:
    bank_account()