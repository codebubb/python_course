def txt():
    person_input = raw_input("What would you like to save? ")
    
    openfile = open(person_input, 'r')
    print "The truth is : ", openfile.read()
    openfile.close()
    txt()

txt()




unix epoc
