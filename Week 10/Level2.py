"""
    Project: Week 10 Assessment
    Author: James Bubb
    Date: 07/04/2016
"""

balance = 0 # Keep track of money in account
transactions = [] # List of transactions that have occurred

def deposit():
    """ Adds the amount to the overall balance """
    global balance, transactions
    amount = get_amount()
    balance += amount
    transactions.append(amount)

def withdraw():
    """ Removes the amount from the overall balance """
    global balance, transactions
    amount = get_amount()
    balance -= amount
    transactions.append(-amount)

def get_amount():
    """ Returns the amount entered by user """
    return int(raw_input("Enter amount"))

def display_balance():
    """ Output the current balance variable """
    global balance
    print "\nCurrent balance is: %d\n" % balance

def display_transactions():
    """ Output the current list of transactions """
    print "\nLatest transactions:"
    global transactions
    for trans in transactions:
        print ">>>", trans

def login(user):
    try:
        with open("accounts/" + user + ".txt", 'r') as f:
            password = f.readline().strip()
            balance = f.readline().strip()
            return (password, int(balance))
    except:
        print "Couldn't read user file."

def write_data(user, password):
    global balance
    try:
        with open("accounts/" + user + ".txt", 'w') as f:
            f.write(password + "\n")
            f.write(str(balance) + "\n")
    except:
        print "Couldn't write to user file."

# Main program
print '''
 _    _      _                            _          _____ ______ _      ______             _    _               _     _           _ _           _
| |  | |    | |                          | |        |  __ \| ___ \ |     | ___ \           | |  (_)             | |   (_)         (_) |         | |
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |  \/| |_/ / |     | |_/ / __ _ _ __ | | ___ _ __   __ _  | |    _ _ __ ___  _| |_ ___  __| |
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | | __ | ___ \ |     | ___ \/ _` | '_ \| |/ / | '_ \ / _` | | |   | | '_ ` _ \| | __/ _ \/ _` |
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_\ \| |_/ / |____ | |_/ / (_| | | | |   <| | | | | (_| | | |___| | | | | | | | ||  __/ (_| |
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \____/\____/\_____/ \____/ \__,_|_| |_|_|\_\_|_| |_|\__, | \_____/_|_| |_| |_|_|\__\___|\__,_|
                                                                                                          __/ |
                                                                                                         |___/

    '''
while True:
    username = raw_input("Enter your username:")
    password, balance = login(username)
    if password == raw_input("Enter your password:"):
        break
    else:
        print "Login failed."
# Provide menu options
while True:
    print """
    Account: %s
    Please select an option:
    ------------------------
    1) Deposit money
    2) Withdraw money
    3) Display balance
    4) Display transactions
    5) Exit

    """ % username

    option = raw_input()

    if option == "5": # User has chosen to quit
        write_data(username, password)
        break
    elif option == "1":
        deposit()
    elif option == "2":
        withdraw()
    elif option == "3":
        display_balance()
    elif option == "4":
        display_transactions()
    else:
        print "Not a valid option, try again."
