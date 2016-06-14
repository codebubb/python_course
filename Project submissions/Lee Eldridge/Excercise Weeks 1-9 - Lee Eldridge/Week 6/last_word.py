def p():
    sentance = raw_input("Please enter a sentance: ")
    list = sentance.split()
    print "The word you are looking for is:", list[-1]
    p()
p()
