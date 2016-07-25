def p():
    sentance = raw_input("Please enter a sentance: ")
    list = sentance.split()
    g(list, sentance)
    
def g(list, sentance):
    place = raw_input("Which position in your sentance do you want to access? ")
    if place.isdigit() == False:
        print "Please only enter numbers."
        g(list, sentance)
        return
    elif int(place) > len(list):
        print "I dont think there are that many words, try again!"
        g(list, sentance)
    
    else:
        pass
    
    place = int(place) - 1
    print "The word you are looking for is:", list[place]
    p()
p()
