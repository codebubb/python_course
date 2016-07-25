import string
print "Hello and welcome to the Software Analaysis Application!"
class software_analysis():
    def __init__(self):
        
        print ""
        print "Here is the menu from here:"
        print "1 - Alphabet Analasis."
        print "2 - Average Length of Sentances."
        print "3 - Extracting Certain Words in Sentances."
        print "Please choose a number:"
        answer = raw_input("")
        if answer == "1":
            self.alphabet()
        elif answer == "2":
            self.average()
        elif answer == "3":
            self.p()
        else:
            print "Please enter either 1, 2 or 3."
            self.__init__()
    

    def alphabet(self):
        print "***************************************************"
        print "Would you like to find out which number a letter \nin the alphabet sits? Well todays your lucky day!"
        print "***************************************************"
        print ""
        count = 0
        menu = raw_input("Would you like to know just ONE letters location? or a BUNCH? ").title()
        print ""
        if menu == "One":
            which_letter = raw_input("Which letter would you like to find out the position of? ").lower()
            if which_letter.isalpha() == False:
                print ""
                print "Please enter a letter."
                print ""
                self.alphabet()
            elif len(which_letter) > 1:
                print ""
                print "Please only enter one letter."
                print ""
                self.alphabet()
            else:
                pass
            print ""
            for e in string.lowercase[:26]:
                count += 1
                if e == which_letter:
                    print e.upper(), "=", count
                    print ""
                    print "You will now be taken back to the main menu."
    
        elif menu == "Bunch":
            number_of_letters = raw_input("From 'A', how many letters would you like to print out? ")
            print ""
            if number_of_letters.isdigit() == False:
                print "Please enter a number between 1-26."
                print ""
                self.alphabet()
                return
            elif int(number_of_letters) > 27:
                print ""
                print "Well, theres only 26 letters in the alphabet soooo... Well heres 26 :)"
                print ""
                number_of_letters = 26
            elif int(number_of_letters) < 27:
                pass
            
            print ""
            number_of_letters = int(number_of_letters)
            for e in string.lowercase[:number_of_letters]:
                count += 1
                print e.upper(), "=", count
            print ""
            print "You will now be taken back to the main menu."
        else:

            print "Please enter either 'One' or 'Bunch'."
            print ""
            self.alphabet()
        self.__init__()

    def average(self):
        average = raw_input("Please enter a sentance and I will word out the average amount of letters of each word! ").title()
        list = average.split()
        sum = 0
        sum = float(sum)
        for e in list:
            sum = float(sum + len(e))
        print ""
        print "Anddddd the average is..."
        print sum / len(list)
        print ""
        print "You will now be taken back to the main menu."
        self.__init__()


    def p(self):
        sentance = raw_input("Please enter a sentance: ")
        list = sentance.split()
        self.g(list, sentance)
    
    def g(self, list, sentance):
        place = raw_input("Which position in your sentance do you want to access? ")
        if place.isdigit() == False:
            print "Please only enter numbers."
            self.g(list, sentance)
            return
        elif int(place) > len(list):
            print "I dont think there are that many words, try again!"
            self.g(list, sentance)
        elif place == "0":
            print "Please enter a number above 0."
            self.g(list, sentance)
            return
        else:
            pass
    
        place = int(place) - 1
        print ""
        print "The word you are looking for is:", list[place]
        print ""
        print "You will now be taken back to the main menu."
        self.__init__()

software_analysis()
