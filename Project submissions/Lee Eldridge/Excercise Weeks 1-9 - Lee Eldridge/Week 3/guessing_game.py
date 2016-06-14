import random
import sys

print "Welcome to the number guessing game!"

player_1 = raw_input("Please enter your name player one: ")
player_2 = raw_input("Please enter your name player two: ")

def p():
    print "%s, your turn." % (player_1)
    guess = raw_input("Guess the number from 1-10 ")
    my_number = int(random.random() * 10) + 1
    guess = int(guess)
    if my_number == guess:
        print "Well done you got the right number!"
        play_again = raw_input("Would you like to play again? ").lower()
        if play_again == "yes":
            p()
        elif play_again == "no":
            print "Game over."
            sys.exit()
        else:
            p()
    elif my_number != guess:
        print "ooo too bad you got it wrong"
        print "%s , your turn." % (player_2)
    guess = raw_input("Guess the number from 1-10 ")
    my_number = int(random.random() * 10) + 1
    guess = int(guess)
    if my_number == guess:
        print "Well done you got the right number!"
        play_again = raw_input("Would you like to play again? ").lower()
        if play_again == "yes":
            p()
        elif play_again == "no":
            print "Game over."
            sys.exit()
        else:
            p()
    elif my_number != guess:
        print "ooo too bad you got it wrong"
    p()
    
p()
