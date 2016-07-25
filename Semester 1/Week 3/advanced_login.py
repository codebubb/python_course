'''
advanced_login.py
-----------------
Compares a given username to see if a user is authorised.
'''

correct_password = "password123"

user_password = raw_input("Please enter your password:")

if user_password == correct_password:
    print "You have logged in successfully!"
else:
    print "Incorrect password."
