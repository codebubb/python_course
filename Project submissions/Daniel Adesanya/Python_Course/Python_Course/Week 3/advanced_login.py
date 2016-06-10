def p():
    password = raw_input("Password Please or GTFO ").lower()
    if password == "please":
        print "Pimping Password Accepted"
        print ""
    elif password == "gtfo":
        print "Boring"
        print ""
    else:
        print "Go outside and Socialse. "
        print ""
    p()
p()
