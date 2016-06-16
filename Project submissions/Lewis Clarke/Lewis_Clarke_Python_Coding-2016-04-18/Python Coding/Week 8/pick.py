import random
while True:
    try:
        list_of_numbers =[]
        for i in range(random.randrange(20)):
            list_of_numbers.append(random.randrange(100))
            pick =int(raw_input("Pick a number you want to display:"))
            print"You picked:", list_of_numbers[pick]
    except IndexError:
        print "That is not a valid index, plese try again"
    
