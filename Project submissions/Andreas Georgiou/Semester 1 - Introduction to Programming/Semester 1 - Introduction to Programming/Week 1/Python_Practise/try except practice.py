while True:
    try:
        number = int(raw_input("Enter a number: "))
        print number
        break
    except ValueError: #(ValueError, IOError): list of exceptions in parentheses (), separated by commas
        print "That is not a number."




try: with open('file.txt', 'r') as f:
    print int(f.readline())
except (ValueError, IOError):
    print "Something went wrong!"




try: with open('file.txt', 'r') as f:
    print int(f.readline())
except IOError:
    print "File could not be opened"
except ValueError:
    print "File contains non-numbers"
finally:
    print "File I/O complete." #finally happenes regardless if exceptions were raised or not.
