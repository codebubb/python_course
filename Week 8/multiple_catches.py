
try:
    with open('file.txt', 'r') as f:
            print int(f.readline())
except (ValueError, IOError):
    print "Something went wrong!"


try:
    with open('file.txt', 'r') as f:
            print int(f.readline())
except IOError:
    print "File could not be opened"
except ValueError:
    print "File contains non-numbers" 
