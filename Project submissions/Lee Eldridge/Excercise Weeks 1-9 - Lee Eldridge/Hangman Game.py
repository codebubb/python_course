import turtle
turtle.right(360)

class Hangman():
    def __init__(self):
        guesses = 0
        print "*" * 80
        print "Welcome to Hangman in Python!"
        print "Hopefully you know the rules by now but if not here it is:"
        print "Guess letters to fill in the blanks before your little man gets hung out to dry."
        print "*" * 80
        print ""
        begin = raw_input("Does that sound simple enough? ").upper()
        print ""
        player_1 = raw_input("Player 1 (the guesser) enter your name: ").title()
        player_2 = raw_input("Player 2 (making the word) enter your name: ").title()
        print ""
        print player_2, "Please enter a word: "
        word = raw_input("").upper()
        print "* \n" * 50
        progress = list("_"*len(word))
        letters_used = []
      
        if begin == ("YES" or "Y"):
            print "Well Lets begin!", player_1, "your turn."
            print ""
            print "Current progress:", progress
            self.game(guesses, word, progress, letters_used)
        elif begin == ("NO" or "N"):
            print "Okay well see ya!"
            exit()
        else:
            while begin != ("YES" or "Y"):
                begin = raw_input("Please enter either YES or NO. ").upper()
                self.game(guesses, word, progress, letters_used)
    
    def game(self, guesses, word, progress, letters_used):
        
        print ""
        while guesses < 7 and not word == "".join(progress):    
            guess = raw_input("Please enter a letter: ").upper()
            if guess in word:
                for x in range(len(word)):
                    if guess == word[x]:
                        progress[x] = guess
                        print "Well done! There is a", guess+"!"
                        print "Current progress:",progress
                        print "Letters used so far:", letters_used
            elif guess not in word:
                guesses += 1
                letters_used.append(guess)
                self.hangman_turtle(guesses, word, progress, guess, letters_used)
            
        print "Well done you saved him! or her? One of them anyways :D."

    def hangman_turtle(self, guesses, word, progress, guess, letters_used):

        if guesses == 1:
            #Bottome Line
            turtle.forward(25)
            turtle.right(180)
            turtle.forward(50)
            turtle.right(180)
            turtle.forward(25)
            turtle.left(90)
            print ""
            print "Oooo, too bad! There is no", guess+"!"
        elif guesses == 2:
            #Main Stand
            turtle.forward(200)
            turtle.right(90)
            print ""
            print "Thats two now! Don't make this a habit! Not", guess+"!"
        elif guesses == 3:
            #Top Line
            turtle.forward(115)
            turtle.right(90)
            turtle.forward(20)
            print ""
            print "You cruel person... Thats three! Not", guess +"!"
        elif guesses == 4:
            #Head
            turtle.penup()
            turtle.right(90)
            turtle.forward(20)
            turtle.left(90)
            turtle.forward(20)
            turtle.pendown()
            turtle.circle(20)
            turtle.penup()
            turtle.forward(20)
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.pendown()
            print ""
            print "FOUR!? Its like you want to kill him :( Not", guess +"!"
        elif guesses == 5:
            #Body
            turtle.forward(70)
            print ""
            print "Might as well stop, hes pretty much dead. Not", guess +"!"
        elif guesses == 6:
            #Arms
            turtle.right(180)
            turtle.forward(60)
            turtle.left(135)
            turtle.forward(40)
            turtle.left(180)
            turtle.forward(40)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(180)
            turtle.forward(40)
            turtle.left(135)
            turtle.forward(60)
            print ""
            print "Poor guy, this is his brutal end. You have ONE LAST CHANCE! Not", guess +"!"
        elif guesses == 7:
            #Legs
            turtle.right(35)
            turtle.forward(60)
            turtle.right(180)
            turtle.forward(60)
            turtle.right(145)
            turtle.left(35)
            turtle.forward(60)
            print ""
            print "I can't belive it... The word was", word +"!"
            print "Too bad looks like he is dead! :("
            print "Hope you're happy now."
            print ""
            print "Good bye!"
            exit()

        print ""
        print "Current progress:",progress
        print "Letters used so far:", letters_used

        self.game(guesses, word, progress, letters_used)




Hangman()



    

