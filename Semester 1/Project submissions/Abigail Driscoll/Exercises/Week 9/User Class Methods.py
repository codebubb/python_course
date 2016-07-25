class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("User created")
    def authenticate(self):
        hidden_password = "password"
        if self.password == hidden_password:
            return True
        else:
            return False
    def get_name(self):
        return self.username

    def get_password(self):
        return self.password

    def get_authenticate(self):
        return self.authenticate


new_user = user("adriscoll", "password")
print(new_user.get_name())
print(new_user.get_password())
if new_user.authenticate():
    print("User has entered correct password and is now logged in")
else:
    print("User has entered incorrect password")
