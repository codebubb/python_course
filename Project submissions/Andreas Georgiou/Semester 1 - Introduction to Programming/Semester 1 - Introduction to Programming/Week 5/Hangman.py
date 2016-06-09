
#####
## Hangman Game
## Designed and Created by Andreas Georgiou
## Python Week 5 Mini-Project
#####

print ""
print "                             +---+       "
print "                             |   |       "
print " ---------------             O   |       "      
print "|               |           /|\  |       "
print "|    Hangman    |           / \  |       "
print "|               |                |       "
print " ---------------            =========    "

print "" # Leaves a gap.

host_name = raw_input("Host - Enter your name:  ").title()
guesser_name = raw_input("Guesser - Enter your name:  ").title()

print ""
print "-", guesser_name, "look away until", host_name, "chooses a word! -"
print ""

host_word = raw_input("Enter a word you would like the guesser to guess:  ").upper()
if str.isalpha(host_word):
    print ""
else:
    print ""
    print "You must enter letters only."
        
for i in range(40):
    print ""

print "                             +---+       "
print "                             |   |       "
print " ---------------             O   |       "      
print "|               |           /|\  |       "
print "|    Hangman    |           / \  |       "
print "|               |                |       "
print " ---------------            =========    "
print ""
print "***", host_name, "<(host) VS (guesser)>", guesser_name, "***"
print ""
print "Rules of the game: Guess", host_name,"'s word letter at a time :D"
print ""

continue1 = raw_input("Type 'Exit' to leave the game or press any button to continue...  ")
if continue1 == exit:
    print "Game Over"
else:
    print ""
    print "Start!"
    print "========================================================================="


def chance1():
    print """
+---+
|   |
    |
    |
    |
    |
========= """

def chance2():
    print """
+---+
|   |
O   |
    |
    |
    |
=========  """

def chance3():
    print """
+---+
|   |
O   |
|   |
    |
    |
========= """

def chance4():
    print """
 +---+
 |   |
 O   |
/|   |
     |
     |
========= """

def chance5():
    print """
 +---+
 |   |
 O   |
/|\  |
     |
     |
========= """

def chance6():
    print """
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========= """

def chance7():
    print """
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========= """


wrong_list = []
progress = list("_" * len(host_word))
guess_count = 1


def l_search():
    
    global guess_count
    print ""
    guess = raw_input("Type the letter you want to guess:  ").upper()
            
    if guess in wrong_list:
        for l in wrong_list:
            if guess == l:
                print "You have already tried that letter, try another letter."

        print ""  
        print "-------------------------------------------------------------------------"
        print ""
        print "CORRECT! You have guessed a letter from the word! Keep going..."
        print ""
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
        print ""
        print "-------------------------------------------------------------------------"
            
    
    elif guess not in host_word and guess_count == 1:
        print "-------------------------------------------------------------------------"
        print chance1()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
    elif guess not in host_word and guess_count == 2:
        print "-------------------------------------------------------------------------"
        print chance2()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
    elif guess not in host_word and guess_count == 3:
        print "-------------------------------------------------------------------------"
        print chance3()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
    elif guess not in host_word and guess_count == 4:
        print "-------------------------------------------------------------------------"
        print chance4()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
    elif guess not in host_word and guess_count == 5:
        print "-------------------------------------------------------------------------"
        print chance5()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
        print ""
        print "You have one more guess! Use it wisley..."
    elif guess not in host_word and guess_count == 6:
        print "-------------------------------------------------------------------------"
        print chance6()
        guess_count += 1
        wrong_list.append(guess)
        print "Your progress so far -", progress
        print "Letters you guessed wrong -", wrong_list
        print ""
    else:
        print "-------------------------------------------------------------------------"
        print ""
        print chance7()
        print "***GAME OVER!***"

       
while "".join(progress) != host_word and guess_count < 7:
    l_search()
