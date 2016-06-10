def p():

    bus_price = int (raw_input("Enter Passenger Age. "))
    if (bus_price > 17) and (bus_price < 65):
        print "Bus Fare is 2.30"
    elif bus_price < 18:
        print "Bus Fare is 1.15"
    elif bus_price >= 65:
        print "Bus Fare is Free"
    p()
p()
