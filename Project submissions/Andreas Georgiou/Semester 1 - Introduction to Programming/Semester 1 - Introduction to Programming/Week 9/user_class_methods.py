import hashlib

class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def encrypt(self):
        hash_pw = hashlib.new("md5")
        hash_pw.update(self.password)
        self.password = hash_pw.hexdigest()

    def authenticate(self):
        if self.password == "482c811da5d5b4bc6d497ffa98491e38":
            print "Authenticated"
            return True
        else:
            print "Incorrect password"
            return False

new_user = user(raw_input("Enter username: "), raw_input("Enter password: "))
new_user.encrypt()
new_user.authenticate()
