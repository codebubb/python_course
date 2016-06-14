print "Welcome to the times table generator! \n"


def p():
    times_table = raw_input("Which times tables would you like to see? ")
    if times_table.isdigit() == False:
        print "Please enter a number."
        p()
    else:
        times_table = int(times_table)
    total = raw_input("Okay, What would you like your times tables to go up to? ")
    if total.isdigit() == False:
        print "Please enter a number."
        p()
    else:
        total = int(total)

    print ""
    
    for x in range(1, total +1):
        print x, "x", times_table, " = ", x * times_table
        
    print ""
    print "This is the %s times tables which go up to %s." % (times_table, total)
    print ""
    print "Now choose your next times tables..."
    p()    

p()
