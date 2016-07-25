class account():
    def __init__(self, account_holder, account_number, account_balance):
        self.account_holder = account_holder
        self.account_number = int(account_number)
        self.account_balance = int(account_balance)
    def get_account_number(self):
        return self.account_number

new_account = account("abi", 10, 1000)
print(new_account.get_account_number())