import hashlib

def log_in():

    pw_file = open("passwordmd5.txt", "r")
    store = pw_file.read()
    pw_file.close()

    user_id = raw_input("Enter User ID: ")
    pw_entry = raw_input("Enter your password: ")
    md5_pw = hashlib.new("md5")
    md5_pw.update(pw_entry)
    if md5_pw.hexdigest() == store and user_id == "Andreas":
        print "\n", "Correct password. Logging in to Andreas's online banking."
    elif md5_pw.hexdigest() == store and user_id == "Python":
        print "\n", "Correct password. Logging in to Pythons online banking."
    else:
        print "\n", "Incorrect User ID or Password. Enter correct login information."
        log_in()

log_in()
