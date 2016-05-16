import hashlib

def encrypt_password(p):
    return hashlib.sha1(p).hexdigest()

# the plaintext 'password' hashed with sha1
stored_password = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'

pwd = raw_input('Please enter your password:')

if encrypt_password(pwd) == stored_password:
    print "Logged in."
else:
    print "Invalid password."
