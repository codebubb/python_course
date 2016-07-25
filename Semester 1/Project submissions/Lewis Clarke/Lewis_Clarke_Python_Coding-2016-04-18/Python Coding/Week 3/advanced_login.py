def password():
    attempts = 3
    while True:
        if attempts <= 3:
            print ("Please enter your password \nYou have %s attempts remaining") % attempts
            password = raw_input("Password: ")
            if password == "password123":
                print ("Your password is correct")
                break
            else:
                print ("your password is incorrect")
                attempts -= 1

        if attempts == 0:
            print ("please contact admin to reset your password")
            break
