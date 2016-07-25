import hashlib
print "Welcome to the program! You will now need to create a login."

def p():
    username = raw_input("Please enter a Username. ")
    if len(username) < 5:
        print "Please enter a Username with atleast 5 characters."
        p()
    password = raw_input("Please enter your Password. ")
    password = hashlib.md5(password).hexdigest() 
    print "Password Accepted and Encrypted."
    print "Your new encrypted password looks like this:", password
    login(password, username)

def login(password, username):
    print ""
    print "Now you have created your login details now login below."
    username_2 = raw_input("Username: ")
    password_2 = raw_input("Password: ")
    if username_2 == username and hashlib.md5(password_2).hexdigest() == password:
        print "Login Successful!"
    else:
        wrong_login(password, username)

def wrong_login(password, username):
    print "Either your username or password is wrong. Please try again."
    username_2 = raw_input("Username: ")
    password_2 = raw_input("Password: ")
    if username_2 == username and hashlib.md5(password_2).hexdigest() == password:
        print "Login Successful!"
        exit()    
    else:
        wrong_login(password, username)
    
p()
