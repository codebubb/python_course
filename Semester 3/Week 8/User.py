class User():
    def __init__(self, name, password):
        # Create a new user object with supplied name and password
        self.name = name
        self.password = password
        self.authenticated = False # Determines whether the user is logged in or not

    def login(self, password):
        # Authenticate user if correct password is supplied
        if password == self.password:
            self.authenticated = True

    def resetPassword(self, newPassword):
        # Reset the password held by the object (only if authenticated)
        if self.authenticated:
            self.password = newPassword
