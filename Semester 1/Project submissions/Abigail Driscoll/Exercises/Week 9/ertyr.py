class user():
    def __init__(self, login_name, password, full_name, department):
        self.login_name = login_name
        self.password = password
        self.full_name = full_name
        self.department = department
        print("User created")
    def get_name(self):
        return self.full_name
    def change_name(self, new_name):
        self.full_name = new_name

new_user = user("adriscoll", "password123", "Abigail Driscoll", "IT")
print(new_user.get_name())
new_user.change_name("Keith Bryers")
print(new_user.get_name())