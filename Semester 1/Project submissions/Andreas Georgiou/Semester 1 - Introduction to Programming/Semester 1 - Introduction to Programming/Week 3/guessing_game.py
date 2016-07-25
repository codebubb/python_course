print ""
print "Guess the number to win the game!"
print ""

import random
my_number = int(random.random() * 10) + 1

print "The number is:", my_number, "Testing puroposes"

def guess():
    user_guess = raw_input("Take a guess? ")
    if user_guess.isdigit() == False:
        print "You must guess a number."
        guess()        
    elif int(user_guess) == my_number:
        print "Well done, you win!"
    else:
        print "Wrong, keep trying!"
        print "--------------------------------"
        guess()

guess()
