print "Welcome to the program! You will now need to login."

def p():
    username = raw_input("Please enter a Username. ")
    if len(username) < 5:
        print "Please enter a Username with atleast 5 characters."
        p()
    password = raw_input("Please enter your Password. ")
    if password == "password123":
        print "Login Successful."
    else:
        print "Incorrect Password."
        return p()

p()
