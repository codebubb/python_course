'''def encrypt_password(str):
    letters = "abcdefghijklmnopqrstuvwxyz" # or string.ascii_lowercase
    encrypted_string = ""
    for char in str.lower():
        pos = letters.index(char)
        if pos > 13: # Stop the index from being out of bounds
            pos -=26
        encrypted_string += letters[pos+13]
    return encrypted_string
'''



'''
def encrypt_password(str):
    letters        = "abcdefghijklmnopqrstuvwxyz" # or string.ascii_lowercase
    rot_13_letters = "nopqrstuvwxyzabcdefghijklm"
    encrypted_string = ""
    for char in str.lower():
         encrypted_string += rot_13_letters[letters.index(char)]
    return encrypted_string


print encrypt_password('password')
'''
# or

import codecs
print codecs.encode('password', 'rot_13')
print codecs.encode('logmein', 'rot_13')
print codecs.encode('letmein', 'rot_13')
