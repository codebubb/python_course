print "Welcome to the bus fare calculator!"
print ""

def p():
    age = raw_input("Please enter the customers age... ")
    if age.isdigit() == False:
        print "Please enter a valid age in years."
    elif int(age) < 18:
        print "The price for an %s year old would be 1.15" % (age)
    elif (age >= "18") and (age <= "64"):
        print "The price for an %s year old would be 2.30" % (age)
    elif age >= "65":
        print "The price for an %s year old would be Free!" % (age)
    print ""
    print "Next customer please!"
    p()

    
p()

