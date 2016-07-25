# user_logins.py
# Log a user in if correct username and password is supplied
users       = ['james', 'matt', 'ronnie', 'stuart']
passwords   = ['jpass', 'mpass', 'rpass', 'spass']

username = raw_input("Please enter your username:")
password = raw_input("Please enter your password:")

valid_user = username in users
valid_password = password in passwords

if valid_user & valid_password:
    if users.index(username) == passwords.index(password):
        print "Logged in."
else:
    print "Invalid login details."
