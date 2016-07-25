# -*- coding: utf-8 -*-
import pickle # For serialisation of data
from hashlib import md5 # Encrypting pins
import time
import os # To clear the screen

class User():
    """ Holds user information about customers """

    def __init__(self, username, pin):
        """ Object constructor """
        self.username = username
        self.pin = pin
        self.file_path = "users/" + self.username + ".txt"

    def write_user_data(self):
        """ Write user data to file """
        userdata = { "pin": md5(self.pin).hexdigest(), "account_type": self.account_type }
        try:
            with open(self.file_path, 'w') as f:
                pickle.dump(userdata, f)
        except:
            print "\nSystem Error: Problem saving user data."

    def load_user_data(self):
        """ Retrieve user data from appropriate file. """
        try:
            with open(self.file_path, 'r') as f:
                userdata = pickle.load(f)
            self.stored_pin = userdata["pin"]
            self.account_type = userdata["account_type"]
        except IOError:
            print "\nUser account error: no user exists"
            exit()
        except:
            print "\nSystem Error: Problem reading user file."

    def authenticated(self):
        """ Returns boolean based on whether user's pin is equal to one stored in file """
        return md5(self.pin).hexdigest() == self.stored_pin

class BankAccount(object):
    """ Hold information about bank accounts held by users """

    def __init__(self, username):
        self.file_path = "accounts/" + username + ".txt"
        try:
            with open(self.file_path, 'r') as f:
                account_data = pickle.load(f)
            self.balance = account_data["balance"]
            self.transactions = account_data["transactions"]
        except:
            print "\nSystem Error: Something went wrong reading account data file."

    def write_account_data(self):
        """ Save account data to file. """
        account_data = { "balance": self.balance, "transactions": self.transactions }
        try:
            with open(self.file_path, 'w') as f:
                pickle.dump(account_data, f)
        except:
            print "\nSystem Error: Something went wrong storing account data."

    def withdraw(self, amount):
        """ Check if balance is available and then subtract amount and add transaction """
        try:
            amount = int(amount)
        except:
            print "\nSystem Error: Invalid amount entered"
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.insert(0, ("DEBIT", amount, time.strftime('%X %x')))
            print "\nWithdrawal successful"
        else:
            print "\nBalanceError: You don't have sufficient funds to make that withdrawal"

    def deposit(self, amount):
        """ Add funds to account, and add transaction. """
        try:
            amount = int(amount)
        except:
            print "\nSystem Error: Invalid amount entered"
        self.balance += amount
        self.transactions.insert(0, ("CREDIT", amount, time.strftime('%X %x')))
        print "\nDeposit successful."

    def display_balance(self):
        """ Rounded balance display to 2 decimal places """
        print "\nCurrent Balance is: ", u'\u00a3', round(self.balance, 2)

    def display_transactions(self):
        """ Tabulated form of transactions. """
        print "\nType\tAmount\tDate"
        print "---------------------------------"
        for trans in self.transactions:
            print trans[0], "\t", u'\u00a3', trans[1], "\t", trans[2]

class StudentAccount(BankAccount):
    """ Inherited from BankAccount but has a large overdraft """

    def __init__(self, username):
        super(StudentAccount, self).__init__(username)
        self.overdraft = 500

    def withdraw(self, amount):
        """ Overrides from BankAccount class to catch overdraft values """
        try:
            amount = int(amount)
        except:
            print "System Error: Invalid amount entered"
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            self.transactions.insert(0, ("DEBIT", amount, time.strftime('%X %x')))
            print "\nWithdrawal Successful."
        else:
            print "BalanceError: You don't have sufficient funds to make that withdrawal"

class SavingsAccount(BankAccount):
    """ Inherited from BankAccount but has a savings function """

    def __init__(self, username):
        self.file_path = "accounts/" + username + ".txt"
        self.interest_period = 600 # Ten minutes
        try:
            with open(self.file_path, 'r') as f:
                account_data = pickle.load(f)
            self.balance = account_data["balance"]
            self.transactions = account_data["transactions"]
            self.interest_rate = account_data["interest_rate"]
            self.last_savings_time = account_data["last_savings_time"]
            if time.time() > self.last_savings_time + self.interest_period:
                self.accrue_savings()
        except:
            print "\nSystem Error: Something went wrong reading account data file."

    def write_account_data(self):
        """ Save extra details like interest rate and last time savings were applied """
        account_data = { "balance": self.balance, "transactions": self.transactions, "interest_rate": self.interest_rate, "last_savings_time": self.last_savings_time }
        try:
            with open(self.file_path, 'w') as f:
                pickle.dump(account_data, f)
        except:
            print "\nSystem Error: Something went wrong storing account data."

    def accrue_savings(self):
        """ Work out how many periods (of self.interest_period seconds) have elapsed since last logon and apply compound savings, adding transactions """
        time_periods_passed = int((time.time() - self.last_savings_time) / self.interest_period)
        for i in range(0, time_periods_passed):
            amount = float(float(self.balance) * float(self.interest_rate) / float(100))
            self.balance += amount
            self.transactions.insert(0, ("INTRST", round(amount,2), time.strftime('%X %x')))
        self.last_savings_time = time.time()
        self.write_account_data

# ------------
# Main program
# ------------
os.system('cls')
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
# Get user object
current_user = User(raw_input("Enter your username: "), raw_input("Enter your pin: "))
# Load pin, account type
current_user.load_user_data()
# Check if the username / pin entered match
if not current_user.authenticated():
    print "\nIncorrect login, exiting..."
    exit()
else:
    # Create an account object based on users account type
    if current_user.account_type == "student":
        account = StudentAccount(current_user.username)
    elif current_user.account_type == "savings":
        account = SavingsAccount(current_user.username)
    else:
        account = BankAccount(current_user.username)

    os.system('cls')
    # --------------
    # Main menu loop
    # --------------
    while True:
        print
        print "-"*100
        print "GBL Banking:", current_user.account_type.title()
        print "-"*100
        print "1) Deposit\n2) Withdraw\n3) Balance\n4) Statement\n5) Exit"

        option = raw_input("Enter an option: ")

        if option == "5":
            # User has chosen to exit, save account data and exit main loop
            account.write_account_data()
            break
        elif option == "4":
            account.display_transactions()
        elif option == "3":
            account.display_balance()
        elif option == "2":
            account.withdraw(raw_input("How much do you want to withdraw?"))
        elif option == "1":
            account.deposit(raw_input("How much do you want to deposit?"))
        else:
            print "Not a valid option, try again"

print "Program finished."
