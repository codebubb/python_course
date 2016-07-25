import hashlib

class user():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def authenticate(self):
        authentication = self.password == "password"
        if authentication == True:
            print ""
            print "User Created.\n\nThese are your login details:"
            print "Username:", self.username
            print "Password:", len(self.password)* "*"
            self.encryption()
        else:
            print "Incorrect password."

    def encryption(self):
        self.password = hashlib.md5(self.password).hexdigest() 
        print "Password Accepted and Encrypted."
        print "Your new encrypted password looks like this:", self.password
            
new_user = user(raw_input("Enter a username: "), raw_input("Enter a password: "))
new_user.authenticate()

