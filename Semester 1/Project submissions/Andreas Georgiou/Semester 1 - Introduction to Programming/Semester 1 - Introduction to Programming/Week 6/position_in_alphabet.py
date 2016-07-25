print ""
print "Alphabet Letters Positions"
print ""
print "(Type 'Return' to proceed to the next test.)"
print "--------"
def alph_position():
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print ""
    pos_of_alph = raw_input("Enter a letter from the alphabet that you want to know the position for: ").upper()
    if len(pos_of_alph) == 1 and pos_of_alph.isalpha():
        print "The position of", pos_of_alph, "in the alphabet is", alph.index(pos_of_alph)+1
        alph_position()
    elif pos_of_alph == "":
        print "Exiting..."
        
    else:
        print "You must enter one letter of the alphabet."
        alph_position()
alph_position()
