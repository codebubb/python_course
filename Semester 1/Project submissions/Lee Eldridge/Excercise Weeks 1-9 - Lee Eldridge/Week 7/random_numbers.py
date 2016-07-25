import random

print "***************************************"
print "Welcome to the random number generator!"
print "***************************************\n"

def p():
    amount_of_random = raw_input("How many random numbers would you like to print? ")
    if amount_of_random.isdigit() == False:
        print ""
        print "Please only enter numbers."
        print ""
        p()
    else:
        d(amount_of_random)

def d(amount_of_random):
    amount_of_minimum = raw_input("What is the minimum value you would like? ")
    if amount_of_minimum.isdigit() == False:
        print ""
        print "Please only enter numbers."
        print ""
        d(amount_of_random)
    else:
        c(amount_of_random, amount_of_minimum)

def c(amount_of_random, amount_of_minimum):
    amount_of_maximum = raw_input("What is the maximum value you would like? ")
    if amount_of_maximum.isdigit() == False:
        print ""
        print "Please only enter numbers."
        print ""
        c(amount_of_random, amount_of_minimum)
    else:
        pass
    
    amount_of_random = int(amount_of_random)
    amount_of_minimum = int(amount_of_minimum)
    amount_of_maximum = int(amount_of_maximum)

    
    print ""    
    for e in range(amount_of_random):
        print random.randrange(amount_of_minimum, amount_of_maximum+1)

    amount_of_maximum = str(amount_of_maximum)
    
    print ""
    print "Andddd here are", amount_of_random, "random numbers between:", amount_of_minimum, "and", amount_of_maximum+"!\n"
    p()
p()
