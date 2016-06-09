print ""
print "Bus Fare Calculator"
print ""

standard = 2.30
under_18 = 1.15
over_64 = 0

def fare():
    print "-----------------------------------------------------"
    traveller_age = raw_input("Enter travellers age: ")
    if traveller_age.isdigit() == False:
        print "You must enter numbers only."
        fare()
    elif int(traveller_age) > 130:
        print "Invalid age, enter valid age."
        fare()
    else:
        traveller_age = int(traveller_age)
    if traveller_age < 18:
        print "The fare for this traveller is $%.2f " % under_18
        fare()
    elif traveller_age > 64:
        print "The fare for this traveller is FREE"
        fare()
    else:
        print "The fare for this traveller is $%.2f " % standard
        fare()
fare()
