class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("User created")
    def get_name(self):
        return self.username
    def get_password(self):
        return self.password


new_user = user("adriscoll", "Password1")

print(new_user.get_name())
print(new_user.get_password())