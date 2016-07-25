import time
open_file = open('text_for_file_reader.txt', 'r')
read = open_file.read()
file_list = read.split()
print read
print ""
print "Hello, currently doing some analysis, please wait..."
time.sleep(3)
print "There are currently:", len(file_list), "words in the above text"
print "There are currently:", len(set(file_list)), "unique words in the above text"


count = 0
for e in file_list:
    count = len(e) + count

print "There are currently:", count, "letters in the above text."

