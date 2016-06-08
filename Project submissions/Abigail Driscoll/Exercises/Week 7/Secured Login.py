import os
import hashlib

f = open('Passwords.txt', 'a')

pwdinput = input("Please enter a password: ").encode('utf-8')
pwd = hashlib.sha1()
pwd.update(pwdinput)
pwd = pwd.hexdigest()
print(pwd)
f.write(pwd + '\n')