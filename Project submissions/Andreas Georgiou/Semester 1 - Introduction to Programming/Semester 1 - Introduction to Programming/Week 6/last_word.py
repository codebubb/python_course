print ""
print "I'll tell you the last word of your sentance"
print ""
print "(Type 'Return' to proceed to the next test.)"
print "--------"

def last_word():
    print ""
    sen = raw_input("Type a sentance: ")
    if sen == "":
        print "Exiting..."
    else:
        for words in sen:
            split_sen = sen.split()
            if len(split_sen) < 2:
                print "You must type two or more words."
                last_word()
        print split_sen[-1]
        last_word()

last_word()
