class user():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print ""
        print "User Created.\n\nThese are your login details:"
        print "Username:", username
        print "Password:", len(password)* "*"
        
new_user = user(raw_input("Enter a username: "), raw_input("Enter a password: "))
