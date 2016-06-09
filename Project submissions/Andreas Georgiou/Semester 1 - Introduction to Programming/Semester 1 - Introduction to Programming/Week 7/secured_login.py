import hashlib

def hash_pw():

    pw_file = open("passwordmd5.txt", "r")
    store = pw_file.read()
    pw_file.close()
        
    pw_entry = raw_input("Enter your password: ")
    md5_pw = hashlib.new("md5")
    md5_pw.update(pw_entry)
    if md5_pw.hexdigest() == store:
        print"Correct password. Logging in..."
    else:
        print "\n", "Incorrect password. Enter correct password."
        hash_pw()

hash_pw()
