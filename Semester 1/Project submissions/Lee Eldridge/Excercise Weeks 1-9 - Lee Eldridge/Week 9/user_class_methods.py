import hashlib
import sys

class user():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def authenticate(self):
        if self.username == "LeeEldridge" and self.password == "password":
            return True
        else:
            return False

    def encryption(self):
        if new_user.authenticate() == True:
            print "\nLogin Completed.\n\nThese are your login details:"
            print "Username:", self.username,"\nPassword:", len(self.password)* "*"
            self.password = hashlib.md5(self.password).hexdigest()
            print "Encrypted password:", self.password
            sys.exit()
        else:
            print "Incorrect username or password."

while True:
    new_user = user(raw_input("Enter a username: "), raw_input("Enter a password: "))
    new_user.encryption()
