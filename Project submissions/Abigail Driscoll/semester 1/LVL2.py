import time

print("Menu")
print("-----")


def login():

    global userid
    userid = input("Please enter your user ID: ")

    # users being Abigail or James

    if userid.lower() == "abigail":
        with open(userid + ".txt", "r") as f:
            global stored_pin
            global stored_balance
            stored_pin = f.readline()
            stored_balance = f.readline()
            f.close()
    elif userid.lower() == "james":
        with open(userid + ".txt", "r") as f:
            stored_pin = f.readline()
            stored_balance = f.readline()
            f.close()
# if incorrect username is entered then the following error message is shown
    else:
        if userid != 'abigail':
            print("Sorry, that user does not exist, please try again")
            login()
        elif userid != 'james':
            print("Sorry, that user does not exist, please try again")
            login()

# store pin and balance so that they can be referenced further into my code

    pin = int(input("Please enter your pin: "))

    if int(stored_pin) == pin:

        # Check that pin user inputted matches pin in txt file
        # users being Abigail or James
        # Abigail pin: 1995 James pin: 2016

        print("Welcome, your balance is: £", stored_balance)

    else:
        print("Sorry, your pin was incorrect, please enter your user ID and try again")
        login()
login()


balance = int(stored_balance)

Wlist = []
Dlist = []

# Empty list to store withdraw and deposit amounts for each session

time_stamp = time.strftime("%d %b %y, %H:%M:%S")

bank = True


def bank_account():
    choice = input("Would you like to deposit(D), withdraw(W), view balance(B), see transactions(T) or exit(E): ")

    if choice.upper() == "W":
        try:
            withdrawal = int(input("How much would you like to withdraw? (£): "))
            with open(userid + ".txt", "r") as f:
                data = f.readlines()
                new_bal = (int(data[1]) - withdrawal)
            if 0 > new_bal > -100:
                print("You are now in your overdraft")
            if new_bal < -100:
                print("Transaction not possible. Your overdraft limit is £100.")
            else:
                print("Your new balance is: £", new_bal)
                Wtotal = '£' + str(withdrawal) + ':' + ' ' + time_stamp
                Wlist.append(Wtotal)
                bank = True

                with open(userid + '.txt', 'r') as f:
                    data = f.readlines()
                    data[1] = str(new_bal)

                with open(userid + '.txt', "w") as f:
                    f.writelines(data)
# Error message for if a character is entered rather than integer
        except ValueError:
            print("Please enter a numerical value")
            bank = True

    if choice.upper() == "D":
        try:
            deposit = int(input("How much would you like to deposit? (£): "))
            with open(userid + ".txt", "r") as f:
                data = f.readlines()
                new_bal = (int(data[1]) + deposit)
            print("Your new balance is: ", new_bal)
            Dtotal = "£" + str(deposit) + ':' + ' ' + time_stamp
            Dlist.append(Dtotal)

            with open(userid + '.txt', 'r') as f:
                data = f.readlines()
                data[1] = str(new_bal)

            with open(userid + '.txt', "w") as f:
                f.writelines(data)
# Error message for if a character is entered rather than integer
        except ValueError:
            print("Please enter a numerical value")
            bank = True

    if choice.upper() == "B":
        with open(userid + ".txt", "r") as f:
            data = f.readlines()
            print("Your balance is: £", data[1])
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
