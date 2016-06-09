class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print "User created"
        print "\n" "(Printing to test..) Username:", username, " | Password:", password

 
new_user = user(raw_input("Enter username: "), raw_input("Enter password: "))
