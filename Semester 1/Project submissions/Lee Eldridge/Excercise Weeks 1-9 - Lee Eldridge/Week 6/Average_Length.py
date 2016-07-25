
def p():

    average = raw_input("Please enter a sentance and I will word out the average amount of letters of each word! ").title()
    
    list = average.split()


    sum = 0
    sum = float(sum)
    for e in list:
        sum = float(sum + len(e))

    print ""
    print "Anddddd the average is..."
    print sum / len(list)
    print ""

    p()
p()
