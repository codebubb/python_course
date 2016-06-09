import random

def rand_num():
    while True:
        try:
            list_of_numbers = []

            for i in range(random.randrange(20)):
                list_of_numbers.append(random.randrange(100))

            print ""
            pick = int(raw_input("Pick a number you want to display:"))

            print "You picked:", list_of_numbers[pick]

        except IndexError:
            print "\n", "The index number you have chosen is our of range. Try choosing another number."
            rand_num()

        except ValueError:
            print "\n", "You must enter a number."
            rand_num()

rand_num()
