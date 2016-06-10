password = raw_input("Enter Password Preety Please? ")
def p():
    if password == "password123" :
        print "Welcome Jackass"
    else:
        print "Wrong Password Fool."
        return p()
p()
