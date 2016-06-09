print "Log in"
print ""

def p():
        password = "password123"
        password_entry = raw_input("Enter your password: ")
        if password_entry == password:
            print "Password accepted. Login in..."
        else:
            print "You have entered an incorrect password. Try again."
            p()

p()
