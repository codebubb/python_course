class BankAccount():
    def __init__(self, balance=0):
        # Initialise bank account with a balanace
        self.balance = balance
        self.transactions = []

    def getBalance(self):
        # Return the value of the current balance
        return self.balance

    def withdraw(self, amount):
        # Return true if the withdrawal is successful, else false
        # Adds an entry to the transactions list if successful
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append("Withdraw: %d" % amount)
            return True
        return False

    def deposit(self, amount):
        # Adds the amount to the account balance
        # Adds an entry to the transaction list
        self.balance += amount
        self.transactions.append("Deposit: %d" % amount)
