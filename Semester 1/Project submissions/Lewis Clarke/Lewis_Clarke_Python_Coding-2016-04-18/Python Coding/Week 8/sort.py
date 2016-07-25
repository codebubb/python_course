try:
    with open(raw_input('Please enter file name: '),'r')as f:
        for line in f:
            numbers = [int(i) for i in line.split()]
        numbers.sort();
        print numbers
except NameError:
    print 'File is not sortable'
except IOError:
    print "File cannot be opened"
except ValueError:
    print "File conatins no numbers"
