'''
file_io.py
----------
Open a file and write some user details to it.
'''
user_input  = raw_input("What do you want to save?")
filename    = 'storage.txt'         # The filename where data will be stored

# To write to a file
open_file   = open(filename, 'w')  # Open file for reading and appending
open_file.write(user_input)
open_file.close()

# To read from a file
open_file   = open(filename, 'r')
while True:
    line = open_file.readline()
    print line, "\n"
    if not line:
        break
open_file.close()
