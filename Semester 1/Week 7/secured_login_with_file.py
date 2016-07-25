import hashlib

def encrypt_password(p):
    return hashlib.sha1(p).hexdigest()

# open file and read in line (containing password)
with open('password.txt', 'r') as f:
    stored_password = f.readline().strip() # really important!

pwd = raw_input('Please enter your password:')

if encrypt_password(pwd) == stored_password:
    print "Logged in."
else:
    print "Invalid password."
