class Account(object):

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


new_user = Account(raw_input('Please enter your username:'),raw_input('Please enter your password: '))
