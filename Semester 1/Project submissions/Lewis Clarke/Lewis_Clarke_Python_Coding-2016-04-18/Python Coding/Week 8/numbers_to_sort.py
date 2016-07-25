try:
    with open('numbers.txt','r')as f:
        for line in f:
            numbers = [int(i) for i in line.split()]
        numbers.sort();
        print numbers
except IOError:
    print "File cannot be opened"
except ValueError:
    print "File conatins no numbers"
