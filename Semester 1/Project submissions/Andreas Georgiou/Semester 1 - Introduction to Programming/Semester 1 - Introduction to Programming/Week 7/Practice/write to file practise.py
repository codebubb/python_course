user_input  = raw_input("Type something to store: ")
filename    = "test.txt"

open_file = open(filename, "w+")
open_file.write(user_input)
open_file.close()
