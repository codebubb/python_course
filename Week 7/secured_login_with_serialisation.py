import hashlib
import pickle

def encrypt_password(p):
    return hashlib.sha1(p).hexdigest()

# open file and read in line (containing password)
with open('serialised_password.txt', 'r') as f:
    stored_password = pickle.load(f)

pwd = raw_input('Please enter your password:')

if encrypt_password(pwd) == stored_password:
    print "Logged in."
    if raw_input("Change Password? (Y/N)").lower() == 'y':
        new_pwd = raw_input("Enter new password:")
        with open('serialised_password.txt', 'w') as f:
            pickle.dump(encrypt_password(new_pwd), f)
else:
    print "Invalid password."
