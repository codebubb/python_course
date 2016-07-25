import codecs
def p():
    secret_code = raw_input("Enter a phrase you would like to be encoded: ")
    print ""
    secret_code = codecs.encode(secret_code, 'rot13')
    print "Encyption Completed."
    print ""
    d(secret_code)
def d(secret_code):
    view = raw_input("Would you like to see your new encrypted password? ").lower()
    if view == "yes":
        print ""
        print "Your encrypted code looks like this:", secret_code
    elif view == "no":
        print ""
        
        print "No problem, it has been stored."
        exit()
    else:
        print ""
        print "Please enter yes or no."
        print ""
        d(secret_code)
p()



