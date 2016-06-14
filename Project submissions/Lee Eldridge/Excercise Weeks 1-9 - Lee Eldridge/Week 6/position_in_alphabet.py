import string
print "***************************************************"
print "Would you like to find out which number a letter \nin the alphabet sits? Well todays your lucky day!"
print "***************************************************"
print ""

def alphabet():
    count = 0
    menu = raw_input("Would you like to know just ONE letters location? or a BUNCH? ").title()
    print ""
    if menu == "One":
        which_letter = raw_input("Which letter would you like to find out the position of? ").lower()
        print ""
        for e in string.lowercase[:26]:
            count += 1
            if e == which_letter:
                print e.upper(), "=", count
                print ""
        
    
    elif menu == "Bunch":
        number_of_letters = int(raw_input("How many letters would you like to print out? "))
        print ""
        if number_of_letters > 27:
            print ""
            print "Well, theres only 26 letters in the alphabet soooo... Well heres 26 :)"
            print ""
            number_of_letters = 26
        elif number_of_letters < 27:
            pass
        else:
            "Please enter a number between 1-26."
        print ""

        for e in string.lowercase[:number_of_letters]:
            count += 1
            print e.upper(), "=", count
    else:
        print ""
        print "Please enter either 'One' or 'Bunch'."
        print ""
    alphabet()
alphabet()
