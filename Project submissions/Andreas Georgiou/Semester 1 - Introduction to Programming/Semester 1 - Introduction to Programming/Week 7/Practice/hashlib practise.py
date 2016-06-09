import hashlib

user_pw = raw_input("Enter your password: ")

hash_pw = hashlib.new("md5") # create a new hash object by using the new function of hashlib specifying the algorithm desired

hash_pw.update(user_pw) # the hash object can be updated with the plaintext you want to encrypt

print hash_pw.hexdigest() # hexdigest method returns the string representation of the encrypted hash



# print hashlib.md5('password').hexdigest()     <---- compact version of above
