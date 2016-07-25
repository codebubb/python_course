import hashlib
import pickle

def password_gen():
    with open('txt_file','wb') as f:
        password = hashlib.md5()
        password.update(raw_input('Create your password here: '))
        f.write (password.hexdigest())

def password_check():
    txt_file = open('txt_file', 'rb')
    user_input = hashlib.md5()
    user_input.update(raw_input('Please enter your password: '))
    for line in txt_file:
        if line == user_input.hexdigest():
            print 'Your password is correct'
        else:
            print 'Password is incorrect please try again'
            password_check()
