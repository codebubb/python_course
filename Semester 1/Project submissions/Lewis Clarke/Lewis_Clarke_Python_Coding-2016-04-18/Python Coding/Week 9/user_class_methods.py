class Account(object):

    def __init__(self,username,password,):
        self.username = username
        self.password = password


    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def auth(self,authenticate):
        if self.username == authenticate:
            return True
        else:
            return False

new_user = Account(raw_input('Please enter your username: '),raw_input('Please enter your password: '))

new_user.auth(raw_input('Please enter your username: '))
